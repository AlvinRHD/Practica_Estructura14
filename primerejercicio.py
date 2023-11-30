import re

def valido_empleado(cadena):
    patron = re.compile(r'^EMP\d{3}$')
    resultado = patron.match(cadena)
    return bool(resultado)

codigo1 = "EMP123"
codigo2 = "EMP345"
codigo3 = "EM123" #No aceptable

print(valido_empleado(codigo1))
print(valido_empleado(codigo2))
print(valido_empleado(codigo3))#No aceptable