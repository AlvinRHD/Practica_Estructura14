import re

def en_ocurrencias(texto, palabra):
    palabra = re.escape(palabra)

    pa_palabra = re.compile(r'\b' + palabra + r'\b', re.IGNORECASE)
    coincidencias_iterador = pa_palabra.finditer(texto)
    ubicaciones_ocurrencias = [coincidencia.span() for coincidencia in coincidencias_iterador]
    return ubicaciones_ocurrencias

text1 = "Este es un ejemplo de texto con una palabra especifica, esta es la palabra especifica, especifica"

buscar = "especifica"
ocurrencias = en_ocurrencias(text1, buscar)

print(f"Ubicaciones de ocurrencias de '{buscar}': {ocurrencias}")