# 1. Nombre del archivo
file_name = "my_notes.txt"

# Crea el archivo
archivo_escritura = open(file_name, "w")

# Escribir en líneas en el archivo
archivo_escritura.write("Línea 1: 6am despertarme\n")
archivo_escritura.write("Línea 2: Voy al gimnasio\n")

#Escribir varias líneas a la vez
lineas = ["Línea 3: Voy a clases\n", "Línea 4: almuerzo\n"]
archivo_escritura.writelines(lineas)

#Cerramos el archivo
archivo_escritura.close()

#Abrir el archivo en modo lectura
archivo_lectura = open(file_name, "r")

#Mostramos en modo lectura
for line in archivo_lectura:
    print(line.strip())  # Quitar el salto de línea al final

#Cerramos el archivo de lectura
archivo_lectura.close()