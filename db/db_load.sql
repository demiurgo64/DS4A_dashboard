COPY datafinaldepurado(estu_tipodocumento,
estu_nacionalidad,
estu_genero,
estu_fechanacimiento,
periodo, 
estu_consecutivo,
estu_estudiante,
estu_depto_reside,
estu_cod_reside_depto, 
estu_mcpio_reside,
estu_cod_reside_mcpio,
estu_cole_termino, 
estu_valormatriculauniversidad,
estu_pagomatriculabeca,
estu_pagomatriculacredito,
estu_pagomatriculapadres,
estu_pagomatriculapropio, 
estu_simulacrotipoicfes,
estu_actividadrefuerzoareas, 
estu_actividadrefuerzogeneric,
estu_tipodocumentosb11,
fami_educacionpadre,
fami_educacionmadre,
fami_estratovivienda,
fami_tieneinternet,
fami_tienecomputador,
fami_tienelavadora,
fami_tieneautomovil,
estu_horassemanatrabaja,
inst_cod_institucion, 
inst_nombre_institucion,
estu_prgm_academico,
estu_prgm_codmunicipio, 
estu_prgm_municipio,
estu_prgm_departamento,
estu_nivel_prgm_academico,
estu_metodo_prgm,
estu_nucleo_pregrado,
estu_inst_codmunicipio,
estu_inst_municipio,
estu_inst_departamento,
inst_caracter_academico,
inst_origen,
estu_cod_mcpio_presentacion, 
estu_mcpio_presentacion,
estu_depto_presentacion,
estu_cod_depto_presentacion, 
mod_razona_cuantitat_punt, 
mod_razona_cuantitativo_pnal, 
mod_lectura_critica_punt, 
mod_lectura_critica_pnal, 
mod_competen_ciudada_punt, 
mod_competen_ciudada_pnal, 
mod_ingles_punt, 
mod_ingles_desem,
mod_ingles_pnal, 
mod_comuni_escrita_punt, 
mod_comuni_escrita_desem, 
mod_comuni_escrita_pnal, 
estu_estadoinvestigacion, 
periodox,
prueba,
tipo_prueba				
--estu_snies_prgmacademico TEXT, --INTEGER 
)
FROM '/home/ubuntu/data/data-final-depurado-fecha.csv' 
DELIMITER ',' CSV HEADER;
