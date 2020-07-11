-- custom sorting
CREATE OR REPLACE FUNCTION custom_sort(anyarray, anyelement)
  RETURNS INT AS 
$$
  SELECT i FROM (
     SELECT generate_series(array_lower($1,1),array_upper($1,1))
  ) g(i)
  WHERE $1[i] = $2
  LIMIT 1;
$$ LANGUAGE SQL IMMUTABLE;


-- prueba
DROP TABLE IF EXISTS dim_prueba;
CREATE TABLE dim_prueba AS
SELECT DISTINCT prueba
FROM datafinaldepurado;


-- modulo
DROP TABLE IF EXISTS dim_modulo;
CREATE TABLE dim_modulo (modulo TEXT);
INSERT INTO dim_modulo VALUES (
    "mod_comuni_escrita_punt",
    "mod_competen_ciudada_punt",
    "mod_lectura_critica_punt",
    "mod_razona_cuantitat_punt",
    "mod_ingles_punt"
);


-- periodo
DROP TABLE IF EXISTS dim_periodo;
CREATE TABLE dim_periodo AS
SELECT DISTINCT prueba, periodo
FROM datafinaldepurado
ORDER BY prueba, periodo;


-- ESTU_PRGM_DEPARTAMENTO
DROP TABLE IF EXISTS fact_estu_prgm_departamento;
CREATE TABLE fact_estu_prgm_departamento AS
SELECT 
  prueba, 
  periodo,
  estu_prgm_departamento,
  AVG(mod_comuni_escrita_punt) AS mod_comuni_escrita_punt,
  AVG(mod_competen_ciudada_punt) AS mod_competen_ciudada_punt,
  AVG(mod_lectura_critica_punt) AS mod_lectura_critica_punt,
  AVG(mod_razona_cuantitat_punt) AS mod_razona_cuantitat_punt,
  AVG(mod_ingles_punt) AS mod_ingles_punt
FROM datafinaldepurado
GROUP BY prueba, periodo, estu_prgm_departamento;

