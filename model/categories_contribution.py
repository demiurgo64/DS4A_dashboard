import pandas as pd


# Saber Pro
pro_comuni = {
    'ESTU_NUCLEO_PREGRADO': 0.18,
    'ESTU_GENERO': 0.05,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.22,
    'INST_ORIGEN': 0.12,
    'FAMI_ESTRATOVIVIENDA': 0.15,
    'INST_CARACTER_ACADEMICO': 0.05,
    'ESTU_METODO_PRGM': 0.03,
    'ESTU_PRGM_DEPARTAMENTO': 0.19
}

pro_compet = {
    'ESTU_NUCLEO_PREGRADO': 0.17,
    'ESTU_GENERO': 0.01,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.27,
    'INST_ORIGEN': 0.11,
    'FAMI_ESTRATOVIVIENDA': 0.16,
    'INST_CARACTER_ACADEMICO': 0.07,
    'ESTU_METODO_PRGM': 0.05,
    'ESTU_PRGM_DEPARTAMENTO': 0.16
}

pro_ingles = {
    'ESTU_NUCLEO_PREGRADO': 0.09,
    'ESTU_GENERO': 0.01,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.28,
    'INST_ORIGEN': 0.09,
    'FAMI_ESTRATOVIVIENDA': 0.33,
    'INST_CARACTER_ACADEMICO': 0.05,
    'ESTU_METODO_PRGM': 0.05,
    'ESTU_PRGM_DEPARTAMENTO': 0.09
}

pro_lectur = {
    'ESTU_NUCLEO_PREGRADO': 0.14,
    'ESTU_GENERO': 0.01,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.32,
    'INST_ORIGEN': 0.09,
    'FAMI_ESTRATOVIVIENDA': 0.13,
    'INST_CARACTER_ACADEMICO': 0.08,
    'ESTU_METODO_PRGM': 0.06,
    'ESTU_PRGM_DEPARTAMENTO': 0.17
}

pro_razona = {
    'ESTU_NUCLEO_PREGRADO': 0.36,
    'ESTU_GENERO': 0.15,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.16,
    'INST_ORIGEN': 0.07,
    'FAMI_ESTRATOVIVIENDA': 0.07,
    'INST_CARACTER_ACADEMICO': 0.05,
    'ESTU_METODO_PRGM': 0.02,
    'ESTU_PRGM_DEPARTAMENTO': 0.11
}

# Saber TyT
tyt_comuni = {
    'ESTU_NUCLEO_PREGRADO': 0.36,
    'ESTU_GENERO': 0.23,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.21,
    'INST_ORIGEN': 0.05,
    'FAMI_ESTRATOVIVIENDA': 0.05,
    'INST_CARACTER_ACADEMICO': 0.04,
    'ESTU_METODO_PRGM': 0.03,
    'ESTU_PAGOMATRICULABECA': 0.01,
    'ESTU_PRGM_DEPARTAMENTO': 0.01
}

tyt_compet = {
    'ESTU_NUCLEO_PREGRADO': 0.36,
    'ESTU_GENERO': 0.23,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.21,
    'INST_ORIGEN': 0.05,
    'FAMI_ESTRATOVIVIENDA': 0.05,
    'INST_CARACTER_ACADEMICO': 0.04,
    'ESTU_METODO_PRGM': 0.03,
    'ESTU_PAGOMATRICULABECA': 0.01,
    'ESTU_PRGM_DEPARTAMENTO': 0.01
}

tyt_ingles = {
    'ESTU_NUCLEO_PREGRADO': 0.36,
    'ESTU_GENERO': 0.23,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.21,
    'INST_ORIGEN': 0.05,
    'FAMI_ESTRATOVIVIENDA': 0.05,
    'INST_CARACTER_ACADEMICO': 0.04,
    'ESTU_METODO_PRGM': 0.03,
    'ESTU_PAGOMATRICULABECA': 0.01,
    'ESTU_PRGM_DEPARTAMENTO': 0.01
}

tyt_lectur = {
    'ESTU_NUCLEO_PREGRADO': 0.36,
    'ESTU_GENERO': 0.23,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.21,
    'INST_ORIGEN': 0.05,
    'FAMI_ESTRATOVIVIENDA': 0.05,
    'INST_CARACTER_ACADEMICO': 0.04,
    'ESTU_METODO_PRGM': 0.03,
    'ESTU_PAGOMATRICULABECA': 0.01,
    'ESTU_PRGM_DEPARTAMENTO': 0.01
}

tyt_razona = {
    'ESTU_NUCLEO_PREGRADO': 0.36,
    'ESTU_GENERO': 0.23,
    'ESTU_VALORMATRICULAUNIVERSIDAD': 0.21,
    'INST_ORIGEN': 0.05,
    'FAMI_ESTRATOVIVIENDA': 0.05,
    'INST_CARACTER_ACADEMICO': 0.04,
    'ESTU_METODO_PRGM': 0.03,
    'ESTU_PAGOMATRICULABECA': 0.01,
    'ESTU_PRGM_DEPARTAMENTO': 0.01
}


# Summary
summary = {
    'SaberPro': {
        'mod_comuni_escrita_punt': pro_comuni,
        'mod_competen_ciudada_punt': pro_compet,
        'mod_lectura_critica_punt': pro_lectur,
        'mod_razona_cuantitat_punt': pro_razona,
        'mod_ingles_punt': pro_ingles
    },
    'SaberTyT': {
        'mod_comuni_escrita_punt': tyt_comuni,
        'mod_competen_ciudada_punt': tyt_compet,
        'mod_lectura_critica_punt': tyt_lectur,
        'mod_razona_cuantitat_punt': tyt_razona,
        'mod_ingles_punt': tyt_ingles
    }
}

df_columns = ['test', 'module', 'factor', 'contribution']
df_rows = []

available_module = [
    "mod_comuni_escrita_punt",
    "mod_competen_ciudada_punt",
    "mod_lectura_critica_punt",
    "mod_razona_cuantitat_punt",
    "mod_ingles_punt"
]

factor_english_names = {
    'estu_nucleo_pregrado': 'Knowledge Area',
    'estu_prgm_departamento': 'Department',
    'estu_genero': 'Gender',
    'fami_estratovivienda': 'Stratum',
    'inst_caracter_academico': 'Institution Level',
    'estu_metodo_prgm': 'Education Method',
    'inst_origen': 'Institution Type',
    'estu_valormatriculauniversidad': 'Tuition cost',
    'estu_simulacrotipoicfes': 'Prepared using mock test',
    'estu_horassemanatrabaja': 'Working hours per week',
    'estu_pagomatriculabeca': 'Scholarship'
}

for test in ("SaberPro", "SaberTyT"):
    for module in available_module:
        for factor, contribution in summary[test][module].items():
            df_rows.append((test, module, factor_english_names[factor.lower()], contribution))

pie_df = pd.DataFrame(df_rows, columns=df_columns)

