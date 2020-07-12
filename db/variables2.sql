-- ESTU_NUCLEO_PREGRADO
DROP TABLE IF EXISTS fact_estu_nucleo_pregrado;
CREATE TABLE fact_estu_nucleo_pregrado AS
SELECT
    prueba,
    year,
    estu_nucleo_pregrado,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, estu_nucleo_pregrado;

-- ESTU_PRGM_DEPARTAMENTO
DROP TABLE IF EXISTS fact_estu_prgm_departamento;
CREATE TABLE fact_estu_prgm_departamento AS
SELECT
    prueba,
    year,
    estu_prgm_departamento,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, estu_prgm_departamento;

-- ESTU_GENERO
DROP TABLE IF EXISTS fact_estu_genero;
CREATE TABLE fact_estu_genero AS
SELECT
    prueba,
    year,
    estu_genero,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, estu_genero;

-- FAMI_ESTRATOVIVIENDA
DROP TABLE IF EXISTS fact_fami_estratovivienda;
CREATE TABLE fact_fami_estratovivienda AS
SELECT
    prueba,
    year,
    fami_estratovivienda,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, fami_estratovivienda;

-- INST_CARACTER_ACADEMICO
DROP TABLE IF EXISTS fact_inst_caracter_academico;
CREATE TABLE fact_inst_caracter_academico AS
SELECT
    prueba,
    year,
    inst_caracter_academico,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, inst_caracter_academico;

-- ESTU_METODO_PRGM
DROP TABLE IF EXISTS fact_estu_metodo_prgm;
CREATE TABLE fact_estu_metodo_prgm AS
SELECT
    prueba,
    year,
    estu_metodo_prgm,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, estu_metodo_prgm;

-- INST_ORIGEN
DROP TABLE IF EXISTS fact_inst_origen;
CREATE TABLE fact_inst_origen AS
SELECT
    prueba,
    year,
    inst_origen,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, inst_origen;

-- ESTU_VALORMATRICULAUNIVERSIDAD
DROP TABLE IF EXISTS fact_estu_valormatriculauniversidad;
CREATE TABLE fact_estu_valormatriculauniversidad AS
SELECT
    prueba,
    year,
    estu_valormatriculauniversidad,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, estu_valormatriculauniversidad;

-- ESTU_SIMULACROTIPOICFES
DROP TABLE IF EXISTS fact_estu_simulacrotipoicfes;
CREATE TABLE fact_estu_simulacrotipoicfes AS
SELECT
    prueba,
    year,
    estu_simulacrotipoicfes,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, estu_simulacrotipoicfes;

-- ESTU_HORASSEMANATRABAJA
DROP TABLE IF EXISTS fact_estu_horassemanatrabaja;
CREATE TABLE fact_estu_horassemanatrabaja AS
SELECT
    prueba,
    year,
    estu_horassemanatrabaja,
    AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
    AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
    AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
    AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
    AVG(mod_ingles_punt) AS mod_ingles_punt,
    MIN(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_min,
    MIN(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_min,
    MIN(mod_lectura_critica_punt) AS mod_lectura_critica_punt_min,
    MIN(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_min,
    MIN(mod_ingles_punt) AS mod_ingles_punt_min,
    MAX(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt_max,
    MAX(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt_max,
    MAX(mod_lectura_critica_punt) AS mod_lectura_critica_punt_max,
    MAX(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt_max,
    MAX(mod_ingles_punt) AS mod_ingles_punt_max,
    COUNT(estu_consecutivo)
FROM datafinaldepurado
GROUP BY prueba, year, estu_horassemanatrabaja;

