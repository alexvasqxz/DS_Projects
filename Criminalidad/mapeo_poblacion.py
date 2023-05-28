poblacion_alcaldias = {
    'ALVARO OBREGON': 759137,
    'AZCAPOTZALCO': 432205,
    'COYOACAN': 614447,
    'IZTACALCO': 404695,
    'IZTAPALAPA': 1835486,
    'GUSTAVO A. MADERO': 1173351,
    'VENUSTIANO CARRANZA': 443704,
    'XOCHIMILCO': 442178,
    'MIGUEL HIDALGO': 414470,
    'CUAUHTEMOC': 545884,
    'BENITO JUAREZ': 434153,
    'TLAHUAC': 392313,
    'TLALPAN': 699928,
    'LA MAGDALENA CONTRERAS': 247622,
    'CUAJIMALPA DE MORELOS': 217686,
    'MILPA ALTA' : 152685,
}

def get_population(value):
    if value in poblacion_alcaldias:
        return poblacion_alcaldias[value]
    return 0

def obtener_rango_edad(edad):
    if edad <= 12:
        return "Niños"
    elif edad <= 19:
        return "Adolescentes"
    elif edad <= 39:
        return "Adultos jóvenes"
    elif edad <= 59:
        return "Adultos de mediana edad"
    elif edad <= 79:
        return "Adultos mayores"
    else:
        return

def mapeo_sexo(sexo):
    if sexo == 'Masculino':
        return 5
    elif sexo == 'Femenino':
        return 10
    else:
        return 0

def mapeo_tipo_persona(tipo):
    if tipo == 'FISICA':
        return 5
    elif tipo == 'MORAL':
        return 10
    else:
        return 0
