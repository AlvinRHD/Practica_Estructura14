import re

def fecha_valida(cadena):
    patron_fecha = re.compile(r'\b(?:0[1-9]|[12][0-9]|3[01])/(?:0[1-9]|1[0-2])/\d{4}\b')#NO ME FUNCIONA
    coincidencia = patron_fecha.search(cadena)
    return bool(coincidencia)

text1 = "La reunion sera el 15/12/2023 en la sala de conferencias UNIVO"
text2 = "No hay nada"
resultado1 = fecha_valida(text1)
resultado2 = fecha_valida(text2)

print(resultado1)
print(resultado2)