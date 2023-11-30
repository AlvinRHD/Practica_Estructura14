import re
#Patron para buscar codigo postal de 5 digitos al principio de una cadena utilizando match
pattern = re.compile(r'^\d{5}')

text = "12345 San Miguel, San Miguel"
resultado = pattern.match(text)

if resultado:
    print(f"Coincidencia encontrada: {resultado.group()}")
else:
    print("No hay coincidencias")


#############################################################################################
#Patron para buscar una palabra que lleve "Python"
pattern=re.compile(r'\bpython\w*', re.IGNORECASE)


text = 'Python es un lenguaje de programaion poderoso.'
resultado = pattern.search(text)

if resultado:
    print(f"Coincidencia encontrada en cualquier lugar: {resultado.group()}")
else:
    print("No hay coincidencias encontradas")



#############################################################################################
#patrin para buscar todas las palrabras de 2 letras
pattern = re.compile(r'\b\w{2}\b')

text= "Hola, soy un texto con algunas palabras cortas como on, o ur que no se que significa pero ponemos texto como te y to y xx"
# text2= "Hola, soy un texto con algunas palabras cortas como on, o ur que no se que significa pero ponemos texto como te y to y xx"
resultado = pattern.findall(text)
# resultado2 = pattern.findall(text2)

print("Todas las coincidencias encontradas: ")
for palabra in resultado:
    print(palabra)
# for palabra in resultado2:
#     print(palabra)



#############################################################################################
#patron para encontrar todas las direcciones de correo en un texto
pattern= re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

text = "Contacto conmigo en correo@example.com o en otro .correo@dominio.com"
text2 = "Contacto conmigo en correo@example22.com o en otro .correo@dominio22.com"
resultado = pattern.finditer(text)
resultado2= pattern.finditer(text2)

print("Direcciones de correo electronico encontrados: ")
for match in resultado:
    print(match.group())

print("Direcciones de correo electronico encontrados2: ")
for match in resultado2:
    print(match.group())

