#import libs and connect to DB
import plotly.express as px
import pandas as pd
import numpy as np
import itertools
from sqlalchemy import create_engine

#create engine for db connection
engine = create_engine('postgresql://postgres:postgres@localhost:5432/icfes')

# list of tests
available_test = [
    "SaberPro",
    "SaberTyT"
]

# list of years
available_year = [
    2016,
    2017,
    2018,
    2019
]

# list of modules
available_module = [
    "mod_comuni_escrita_punt",
    "mod_competen_ciudada_punt",
    "mod_lectura_critica_punt",
    "mod_razona_cuantitat_punt",
    "mod_ingles_punt"
]

# list of factors
available_factor = [
    'estu_prgm_departamento',
    'estu_metodo_prgm',
    'inst_caracter_academico',
    'inst_origen',
    'estu_nucleo_pregrado',
    'estu_valormatriculauniversidad',
    'estu_genero',
    'estu_horassemanatrabaja',
    'estu_simulacrotipoicfes',
    'fami_estratovivienda'
]

# create table for boxplot stats
query = '''
	DROP TABLE IF EXISTS boxplots_stats;
	CREATE TABLE boxplots_stats (
	test TEXT, 
	year INTEGER, 
	module TEXT,
	factor TEXT,
	level TEXT,
	mean FLOAT,
	median FLOAT,
	q1 FLOAT,
	q3 FLOAT,
	lowerfence FLOAT,
	upperfence FLOAT
	);
'''

with engine.connect() as con:
	rs = con.execute(query)
	
# create table for boxplot outliers
query = '''
	DROP TABLE IF EXISTS boxplots_outliers;
	CREATE TABLE boxplots_outliers (
	test TEXT, 
	year INTEGER, 
	module TEXT,
	factor TEXT,
	level TEXT,
	outlier FLOAT
	);
'''
with engine.connect() as con:
	rs = con.execute(query)
	
# iterate over all possible combinations of test, year, module, factor
for selected_test, selected_year, selected_mod, selected_factor in itertools.product(available_test, available_year, available_module, available_factor): 
	print("""Generating boxplot data for test {0}, year {1}, module {2}, factor {3}""".format(selected_test, selected_year, selected_mod, selected_factor))
	#query result subset for boxplot
	#selected_test = 'SaberPro'
	#selected_year = 2017
	#selected_mod = 'mod_comuni_escrita_punt'
	#selected_factor = 'fami_estratovivienda'
	print("Gathering data...")
	query = '''
		SELECT {3}, {0} 
		FROM datafinaldepurado 
		WHERE prueba = '{1}' 
		AND year = {2}
	'''.format(selected_mod, selected_test, selected_year, selected_factor)

	filtered_df = pd.read_sql_query(query,con=engine)
	filtered_df.dropna(inplace=True)


	# compute stats for boxplot and combine into single df joining by index
	print("Computing summary stats...")
	means = filtered_df.groupby([selected_factor]).mean()
	medians = filtered_df.groupby([selected_factor]).median()
	q1s = filtered_df.groupby([selected_factor]).quantile(0.25)
	q3s = filtered_df.groupby([selected_factor]).quantile(0.75)
	lowerfences = q1s - (q3s-q1s)*1.5 
	upperfences = q3s + (q3s-q1s)*1.5 

	stats = means.copy()
	stats.rename(columns={selected_mod: 'means'}, inplace=True, errors="raise")
	stats = stats.join(medians)
	stats.rename(columns={selected_mod: 'medians'}, inplace=True, errors="raise")
	stats = stats.join(q1s)
	stats.rename(columns={selected_mod: 'q1s'}, inplace=True, errors="raise")
	stats = stats.join(q3s)
	stats.rename(columns={selected_mod: 'q3s'}, inplace=True, errors="raise")
	stats = stats.join(lowerfences)
	stats.rename(columns={selected_mod: 'lowerfences'}, inplace=True, errors="raise")
	stats = stats.join(upperfences)
	stats.rename(columns={selected_mod: 'upperfences'}, inplace=True, errors="raise")


	# insert stats into DB stats table
	print("Saving summary stats...")
	for i in range(0, len(stats)):
		query = '''
			INSERT INTO boxplots_stats VALUES('{0}', {1}, '{2}', '{3}', '{4}', {5}, {6}, {7}, {8}, {9}, {10});
		'''.format(selected_test, selected_year, selected_mod, selected_factor, stats.index[i], \
				  stats.loc[stats.index[i], 'means'], stats.loc[stats.index[i], 'medians'], \
				  stats.loc[stats.index[i], 'q1s'], stats.loc[stats.index[i], 'q3s'], \
				  stats.loc[stats.index[i], 'lowerfences'], stats.loc[stats.index[i], 'upperfences'])
		with engine.connect() as con:
			rs = con.execute(query)
			
			
	# compute outliers
	print("Computing outliers...")
	names = stats.index.to_numpy()
	outliers = np.empty(len(medians), dtype=object)
	for i, name in enumerate(names):
		outliers[i] = filtered_df.loc[(filtered_df[selected_factor]==name) & \
							   ((filtered_df[selected_mod]>upperfences.loc[name,selected_mod]) |
							   (filtered_df[selected_mod]<lowerfences.loc[name,selected_mod]))
							   , selected_mod].to_numpy()
							   

	# insert outliers in db 
	print("Saving outliers...")
	for i, name in enumerate(names):
		for j in range(len(outliers[i])):
			query = '''
			INSERT INTO boxplots_outliers VALUES('{0}', {1}, '{2}', '{3}', '{4}', {5});
			'''.format(selected_test, selected_year,selected_mod, selected_factor, name, outliers[i][j])
			with engine.connect() as con:
				rs = con.execute(query)