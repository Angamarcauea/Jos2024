# Crear un diccionario con información  personal
informacion_personal = {
    "nombre": "Joselyn Angamarca",
    "edad": 22,
    "ciudad": "Ibarra",
    "profesion": "Estudiante",
    "sexo": "Femenino"
}

# Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal["ciudad"] = "Quito"

# Modificar una clave-valor al diccionario
informacion_personal["edad"] = "24"

# Verificar si la clave "Celular" existe en el diccionario
if "celular" not in informacion_personal:
    informacion_personal["celular"] = "1127524830"  # Agregar número de teléfono

# Eliminar la clave "sexo" del diccionario
informacion_personal["sexo"] = "femenino"

# Imprimir el diccionario
# Imprimir el diccionario resultante
print(informacion_personal)