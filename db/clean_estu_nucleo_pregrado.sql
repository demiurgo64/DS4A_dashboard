ALTER TABLE datafinaldepurado
RENAME COLUMN estu_nucleo_pregrado to estu_nucleo_pregrado_old

ALTER TABLE datafinaldepurado
ADD COLUMN estu_nucleo_pregrado TEXT;
									
UPDATE datafinaldepurado
SET estu_nucleo_pregrado = trim(regexp_replace(estu_nucleo_pregrado_old, '[^[:alpha:]\s]', '', 'g'))
