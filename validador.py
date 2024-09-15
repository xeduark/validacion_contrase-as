import string

def validar_contraseña(contraseña):
    """Valida si una contraseña cumple con ciertos criterios de seguridad y proporciona un informe de errores.

    Args:
        contraseña (str): La contraseña a validar.

    Returns:
        tuple: Un booleano indicando si la contraseña es válida y una lista de errores (si los hay).
    """

    # Criterios de seguridad:
    longitud_minima = 8
    caracteres_especiales = string.punctuation

    # Inicializar variables de control
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False

    errores = []

    # Verificar longitud
    if len(contraseña) < longitud_minima:
        errores.append(f"La contraseña debe tener al menos {longitud_minima} caracteres.")

    # Verificar cada carácter
    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_especial = True

    # Verificar si se cumplen todos los criterios
    if not tiene_mayuscula:
        errores.append("La contraseña debe contener al menos una letra mayúscula.")
    if not tiene_minuscula:
        errores.append("La contraseña debe contener al menos una letra minúscula.")
    if not tiene_numero:
        errores.append("La contraseña debe contener al menos un número.")
    if not tiene_especial:
        errores.append("La contraseña debe contener al menos un carácter especial.")

    es_valida = len(errores) == 0
    return es_valida, errores

# Solicitar contraseña al usuario
contraseña = input("Ingrese su contraseña: ")

# Validar la contraseña
es_valida, errores = validar_contraseña(contraseña)
if es_valida:
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida. Debe cumplir con los siguientes criterios:")
    for error in errores:
        print(f"- {error}")