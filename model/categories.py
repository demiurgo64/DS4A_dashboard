#Mappings

# Quartile group
cat_q ={'Q1': 0, 'Q2': 1, 'Q3': 2, 'Q4': 3}

# Gender
cat_gender = {'F': 0, 'M': 1}

# Origen
cat_inst_type = {'NO OFICIAL - CORPORACIÓN': 0, 'NO OFICIAL - FUNDACIÓN': 1, 
                'OFICIAL DEPARTAMENTAL': 2, 'OFICIAL MUNICIPAL': 3, 'OFICIAL NACIONAL': 4, 
                'REGIMEN ESPECIAL': 5}

# Yes No
cat_yes_no = {'No': 0, 'Si': 1}

# Stratum
cat_stratum = {'Estrato 0': 0, 'Estrato 1': 1, 'Estrato 2': 2, 'Estrato 3': 3, 'Estrato 4': 4, 
                'Estrato 5': 5, 'Estrato 6': 6, 'Sin Estrato': 7}

# Parent Education
cat_parent_education = {'Educación profesional completa': 0, 'Educación profesional incompleta': 1, 
                        'Ninguno': 2, 'No sabe': 3, 'Postgrado': 4, 'Primaria completa': 5, 
                        'Primaria incompleta': 6, 'Secundaria (Bachillerato) completa': 7, 
                        'Secundaria (Bachillerato) incompleta': 8, 'Técnica o tecnológica completa': 9, 
                        'Técnica o tecnológica incompleta': 10}


# Education Method
cat_method = {'DISTANCIA': 0, 'DISTANCIA VIRTUAL': 1, 'PRESENCIAL': 2}

# Institution Level
cat_inst_level = {'INSTITUCIÓN TECNOLÓGICA': 0, 'INSTITUCIÓN UNIVERSITARIA': 1, 'TÉCNICA PROFESIONAL': 2, 'UNIVERSIDAD': 3}

# Work hours/week
cat_work_week_hours = {0: 0, 'Entre 11 y 20 horas': 1, 'Entre 21 y 30 horas': 2, 
                        'Menos de 10 horas': 3, 'Más de 30 horas': 4}

# Valor Matrícula Universidad
cat_tuition_cost = {'Entre 1 millón y menos de 2.5 millones': 0, 'Entre 2.5 millones y menos de 4 millones': 1, 
                    'Entre 4 millones y menos de 5.5 millones': 2, 'Entre 5.5 millones y menos de 7 millones': 3, 
                    'Entre 500 mil y menos de 1 millón': 4, 'Mas de 7 millones': 5, 'Menos de 500 mil': 6, 
                    'Más de 7 millones': 7, 'No pagó matrícula': 8}

# Nucleo
cat_area = {'ADMINISTRACIÓN': 0, 'AGRONOMÍA': 1, 'ANTROPOLOGÍA, ARTES LIBERALES': 2, 'ARQUITECTURA': 3, 
            'ARTES PLÁSTICAS, VISUALES Y AFINES': 4, 'ARTES REPRESENTATIVAS': 5, 'BACTERIOLOGÍA': 6, 
            'BIBLIOTECOLOGÍA, OTROS DE CIENCIAS SOCIALES Y HUMANAS': 7, 'BIOLOGÍA, MICROBIOLOGÍA Y AFINES': 8, 
            'CIENCIAS POLÍTICAS, RELACIONES INTERNACIONALES': 9, 'COMUNICACIÓN SOCIAL, PERIODISMO Y AFINES': 10, 
            'CONTADURÍA PUBLICA': 11, 'DEPORTES, EDUCACIÓN FÍSICA Y RECREACIÓN': 12, 'DERECHO Y AFINES': 13, 
            'DISEÑO': 14, 'ECONOMÍA': 15, 'EDUCACIÓN': 16, 'ENFERMERÍA': 17, 'FILOSOFÍA, TEOLOGÍA Y AFINES': 18, 
            'FORMACIÓN RELACIONADA CON EL CAMPO MILITAR O POLICIAL': 19, 'FÍSICA': 20, 'GEOGRAFÍA, HISTORIA': 21, 
            'GEOLOGÍA, OTROS PROGRAMAS DE CIENCIAS NATURALES': 22, 'INGENIERÍA ADMINISTRATIVA Y AFINES': 23, 
            'INGENIERÍA AGROINDUSTRIAL, ALIMENTOS Y AFINES': 24, 'INGENIERÍA AGRONÓMICA, PECUARIA Y AFINES': 25, 
            'INGENIERÍA AGRÍCOLA, FORESTAL Y AFINES': 26, 'INGENIERÍA AMBIENTAL, SANITARIA Y AFINES': 27, 
            'INGENIERÍA BIOMÉDICA Y AFINES': 28, 'INGENIERÍA CIVIL Y AFINES': 29, 'INGENIERÍA DE MINAS, METALURGIA Y AFINES': 30, 
            'INGENIERÍA DE SISTEMAS, TELEMÁTICA Y AFINES': 31, 'INGENIERÍA ELECTRÓNICA, TELECOMUNICACIONES Y AFINES': 32, 
            'INGENIERÍA ELÉCTRICA Y AFINES': 33, 'INGENIERÍA INDUSTRIAL Y AFINES': 34, 'INGENIERÍA MECÁNICA Y AFINES': 35, 
            'INGENIERÍA QUÍMICA Y AFINES': 36, 'INSTRUMENTACIÓN QUIRÚRGICA': 37, 'LENGUAS MODERNAS, LITERATURA, LINGÜÍSTICA Y AFINES': 38, 
            'MATEMÁTICAS, ESTADÍSTICA Y AFINES': 39, 'MEDICINA': 40, 'MEDICINA VETERINARIA': 41, 'MÚSICA': 42, 'NUTRICIÓN Y DIETÉTICA': 43, 
            'ODONTOLOGÍA': 44, 'OPTOMETRÍA, OTROS PROGRAMAS DE CIENCIAS DE LA SALUD': 45, 'OTRAS INGENIERÍAS': 46, 
            'OTROS PROGRAMAS ASOCIADOS A BELLAS ARTES': 47, 'PSICOLOGÍA': 48, 'PUBLICIDAD Y AFINES': 49, 'QUÍMICA Y AFINES': 50, 
            'SALUD PÚBLICA': 51, 'SOCIOLOGÍA, TRABAJO SOCIAL Y AFINES': 52, 'TERAPIAS': 53, 'ZOOTECNIA': 54}

# Departamento
cat_dpto = {'AMAZONAS': 0, 'ANTIOQUIA': 1, 'ARAUCA': 2, 'ATLANTICO': 3, 'BOGOTA': 4, 'BOLIVAR': 5, 'BOYACA': 6, 
            'CALDAS': 7, 'CAQUETA': 8, 'CASANARE': 9, 'CAUCA': 10, 'CESAR': 11, 'CHOCO': 12, 'CORDOBA': 13, 
            'CUNDINAMARCA': 14, 'GUAVIARE': 15, 'HUILA': 16, 'LA GUAJIRA': 17, 'MAGDALENA': 18, 'META': 19, 
            'NARIÑO': 20, 'NORTE SANTANDER': 21, 'PUTUMAYO': 22, 'QUINDIO': 23, 'RISARALDA': 24, 'SANTANDER': 25, 
            'SUCRE': 26, 'TOLIMA': 27, 'VALLE': 28}

# Year
cat_year = {2016: 0, 2017: 1, 2018: 2, 2019: 3}

# -----------------
# Graph Functions

#  'ESTU_GENERO','INST_ORIGEN','FAMI_TIENEAUTOMOVIL','FAMI_TIENELAVADORA','FAMI_TIENECOMPUTADOR','FAMI_TIENEINTERNET',
#  'FAMI_ESTRATOVIVIENDA','FAMI_EDUCACIONMADRE', 'FAMI_EDUCACIONPADRE','ESTU_METODO_PRGM','INST_CARACTER_ACADEMICO',
#  'ESTU_HORASSEMANATRABAJA','ESTU_ACTIVIDADREFUERZOGENERIC','ESTU_ACTIVIDADREFUERZOAREAS', 'ESTU_SIMULACROTIPOICFES',
#  'ESTU_PAGOMATRICULAPROPIO','ESTU_PAGOMATRICULAPADRES','ESTU_PAGOMATRICULACREDITO','ESTU_PAGOMATRICULABECA',
#  'ESTU_VALORMATRICULAUNIVERSIDAD', 'ESTU_PRGM_DEPARTAMENTO','ESTU_NUCLEO_PREGRADO','PERIODO-X'

def get_feature_vector(selected_dpto, selected_gender, selected_stratum, selected_inst_type, 
                    selected_area, selected_tuition, has_scholarship, selected_level):
    
    try: 
        # Feature vector following training order
        vector = [
            cat_gender[selected_gender],
            cat_inst_type[selected_inst_type],
            cat_yes_no['No'],
            cat_yes_no['No'],
            cat_yes_no['No'],
            cat_yes_no['No'],
            cat_stratum[selected_stratum],
            cat_parent_education['Educación profesional completa'],
            cat_parent_education['Educación profesional completa'],
            cat_method['PRESENCIAL'],
            cat_inst_level[selected_level],
            cat_work_week_hours[0],
            cat_yes_no['No'],
            cat_yes_no['No'],
            cat_yes_no['No'],
            cat_yes_no['No'],
            cat_yes_no['No'],
            cat_yes_no['No'],
            cat_yes_no[has_scholarship],
            cat_tuition_cost[selected_tuition],
            cat_dpto[selected_dpto],
            cat_area[selected_area],
            cat_year[2017]
        ]
    except:
        vector = [0] * 23

    return vector
