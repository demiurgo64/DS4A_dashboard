UPDATE datafinaldepurado
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3
WHERE prueba = 'SaberTyT';

UPDATE boxplots_outliers
SET outlier = 2*outlier/3
WHERE test = 'SaberTyT';

UPDATE boxplots_stats
SET
    mean = 2*mean/3,
    median = 2*median/3,
    q1 = 2*q1/3,
    q3 = 2*q3/3,
    lowerfence = 2*lowerfence/3,
    upperfence = 2*upperfence/3
WHERE test = 'SaberTyT';


UPDATE fact_estu_nucleo_pregrado
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

UPDATE fact_estu_prgm_departamento
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

UPDATE fact_estu_genero
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

UPDATE fact_fami_estratovivienda
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

UPDATE fact_inst_caracter_academico
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

UPDATE fact_estu_metodo_prgm
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

UPDATE fact_inst_origen
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

UPDATE fact_estu_valormatriculauniversidad
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

UPDATE fact_estu_simulacrotipoicfes
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

UPDATE fact_estu_horassemanatrabaja
SET
    mod_comuni_escrita_punt = 2*mod_comuni_escrita_punt/3,
    mod_competen_ciudada_punt = 2*mod_competen_ciudada_punt/3,
    mod_lectura_critica_punt = 2*mod_lectura_critica_punt/3,
    mod_razona_cuantitat_punt = 2*mod_razona_cuantitat_punt/3,
    mod_ingles_punt = 2*mod_ingles_punt/3,
    mod_comuni_escrita_punt_min = 2*mod_comuni_escrita_punt_min/3,
    mod_competen_ciudada_punt_min = 2*mod_competen_ciudada_punt_min/3,
    mod_lectura_critica_punt_min = 2*mod_lectura_critica_punt_min/3,
    mod_razona_cuantitat_punt_min = 2*mod_razona_cuantitat_punt_min/3,
    mod_ingles_punt_min = 2*mod_ingles_punt_min/3,
    mod_comuni_escrita_punt_max = 2*mod_comuni_escrita_punt_max/3,
    mod_competen_ciudada_punt_max = 2*mod_competen_ciudada_punt_max/3,
    mod_lectura_critica_punt_max = 2*mod_lectura_critica_punt_max/3,
    mod_razona_cuantitat_punt_max = 2*mod_razona_cuantitat_punt_max/3,
    mod_ingles_punt_max = 2*mod_ingles_punt_max/3
WHERE prueba = 'SaberTyT';

