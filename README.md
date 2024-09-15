# validacion_contrase-as
Examen Nuevas Tecnologías semana#6

# Validación de Contraseñas

Este repositorio contiene un programa en Python que valida si una contraseña cumple con ciertos criterios de seguridad. A continuación se describen los pasos para implementar el programa y las instrucciones para su uso.

## Criterios de Validación

La contraseña debe cumplir con los siguientes criterios:

- **Longitud mínima**: 8 caracteres.
- **Mayúsculas**: Al menos una letra mayúscula.
- **Minúsculas**: Al menos una letra minúscula.
- **Números**: Al menos un número.
- **Caracteres especiales**: Al menos un carácter especial (!@#$%^&*).

## Pasos para la Implementación

1. **Crear un repositorio en GitHub**:
    - Nombra el repositorio `validacion_contraseñas`.
    - Inicializa el repositorio con un archivo `README.md`.

2. **Crear un archivo Python**:
    - Crea un archivo llamado `validador.py` dentro del repositorio.

3. **Implementar la lógica de validación**:
    - Define una función llamada `validar_contraseña` que reciba la contraseña como argumento.
    - Utiliza ciclos `for` para iterar sobre cada carácter de la contraseña.
    - Utiliza condicionales `if` para verificar cada criterio de la contraseña:
        - Longitud mínima.
        - Mayúsculas.
        - Minúsculas.
        - Números.
        - Caracteres especiales.
    - Si la contraseña cumple con todos los criterios, retorna `True`.
    - Si no cumple, retorna `False`.

4. **Solicitar contraseña al usuario**:
    - Escribe un código que solicite al usuario ingresar una contraseña.

5. **Llamar a la función de validación**:
    - Llama a la función `validar_contraseña` con la contraseña ingresada por el usuario.

6. **Mostrar resultado**:
    - Imprime un mensaje indicando si la contraseña es válida o no.

7. **Comprobar código**:
    - Prueba el código con diferentes contraseñas para asegurarte de que funciona correctamente.

8. **Documentar el código**:
    - Agrega comentarios al código para explicar su funcionamiento.

9. **Subir los cambios a GitHub**:
    - Guarda los cambios y súbelos al repositorio en GitHub.
    - Agrega un commit con un mensaje descriptivo.
    - Empuja los cambios al repositorio remoto.

## Ayuda

- Puedes utilizar la función `len()` para obtener la longitud de la contraseña.
- Puedes utilizar las funciones `isupper()`, `islower()` y `isdigit()` para verificar el tipo de carácter.
- Puedes crear una lista de caracteres especiales para verificar su presencia.
- Utiliza la función `print()` para mostrar mensajes al usuario.
