import re
from datetime import datetime

def validacionNombre(nombre):
    if len(nombre) > 40:
        return False
    
    if not re.match("^[a-zA-Z]+$", nombre):
        return False
    
    return True

def validacionApellido(apellido):
    if len(apellido) > 40:
        return False
    
    if not re.match("^[a-zA-Z]+$", apellido):
        return False
    
    return True

def validar_edad(edad):
    try:
        edad = int(edad)
        if 18 <= edad <= 120:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_nacimiento(fecha_str):
    try:
        # Intenta convertir la cadena de fecha al formato especificado
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        # Verifica si la fecha es válida
        if fecha.year < 1920 or fecha.date() > datetime.now().date():
            return False
        return True
    except ValueError:
        return False

def validar_correo(correo, confirmar_correo):
    if correo == confirmar_correo:
        return True
    else:
        return False