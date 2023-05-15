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
