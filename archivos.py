# Lectura de archgivos
file = open("spider.txt")
#print(file.readline()) # Lee una línea del archivo
#print(file.readline()) # Lee otra línea del archivo
#print(file.read()) # Lee el resto del archivo
# Cierre del archivo
file.close()

# Verificación de si el archivo se puede abrir
with open("spider.txt", "r") as file:
        #print(file.read())
        pass
        
# El archivo se cierra automáticamente al salir del bloque with


# Podemos iterar a través de las lineas de un arcihvo de texto.
with open("spider.txt", "r") as file:
    for line in file:
        print(line.upper())
# Podemos usar el método readlines() para leer todas las líneas del archivo y almacenarlas en una lista.

with open("spider.txt", "r") as file:
    for line in file:
        print(line.strip().upper()) # El método strip() elimina los espacios en blanco al principio y al final de cada línea.
        

# Escritura de archivos (Escrive en un archivo eliminando el contenido anterior)
with open("spider.txt", "w") as file:
    file.write("Hola, mundo!\n")
    file.write("Esta es una nueva línea.\n")


# Alternativamente, podemos usar el modo "a" para añadir contenido al final del archivo sin sobrescribirlo.
with open("spider.txt", "a") as file:
    file.write("Añadiendo una nueva línea al final del archivo.\n")
 
    
# Podemos tambien usar r+ para leer y escribir en el mismo archivo.
with open("spider.txt", "r+") as file:
    content = file.read()
    print("Contenido original:")
    print(content)
    
    file.write("Añadiendo una línea al final del archivo.\n")
    
    file.seek(0)  # Volver al principio del archivo
    updated_content = file.read()
    print("Contenido actualizado:")
    print(updated_content)
