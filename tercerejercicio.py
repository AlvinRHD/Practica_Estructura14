import re 

def minusculas(texto):
    pal_minusculas = re.compile(r'\b[a-z]+\b')
    coincidencias = pal_minusculas.findall(texto)

    return coincidencias

text1 = "Este es un ejemplo de texto con algunas PALABRAS en minusculas y mayusculas"

resultado = minusculas(text1)
print("Palabras encontradas: ", resultado)
