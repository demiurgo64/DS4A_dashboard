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

DROP TABLE IF EXISTS boxplots_outliers;
CREATE TABLE boxplots_outliers (
test TEXT, 
year INTEGER, 
module TEXT,
factor TEXT,
level TEXT,
outlier FLOAT
);

COPY boxplots_stats(test,year,module,factor,level,mean,median,q1,q3,lowerfence,upperfence) 
FROM '/home/ubuntu/data/boxplots_stats_db.csv' 
DELIMITER ',' 
CSV HEADER
ENCODING 'UTF8';

COPY boxplots_outliers(test,year,module,factor,level,outlier) 
FROM '/home/ubuntu/data/boxplots_outliers_db.csv' 
DELIMITER ',' 
CSV HEADER
ENCODING 'UTF8';
