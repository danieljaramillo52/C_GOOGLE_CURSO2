### Para ejecutar Python desde la terminal de Linux usando Windows. 

1. Abrimos cmd
2. Abrimos una nueva pestaña seleccionamos Ubuntu. (Nos abre la ventana nos lleva al root)
3. Podemos ver los discos (En este caso) al disco local c así : `ls /mnt`
4. Podemos ahora acceder a el con `cd /mnt/c`
5. Desplegamos archivos de una carpeta con `ls` nos movemos a traves de los usuarios al directorio de nuestra preferencia. 

6. Ruta:  cd "/mnt/c/Users/DanielJaramilloBusta/Onedrive - XPERTGROUP S.A.S"

7. Ruta directa curso: pwd

cd "/mnt/c/Users/DanielJaramilloBusta/Onedrive - XPERTGROUP S.A.S/Xpert Group Cursos/Certificación Google_automatización_python/Curso 2_python_con_interfaz"

7.1 **Ruta directa al curso desde pc personal:**

cd "/mnt/c/Users/ovejo/Documents/Xpert-group/Cursos XpertGroup/Certificacion GOOGLE automatizacion python/C_GOOGLE_CURSO2"

#### Consultar ruta actual: comando pwd:


### Editor de código. 
- Podemos abir el editor de texto para crear scritps con el comando `Nano` 
- Inmediatamente entramos a la ventana del editor de código. Solo debemos emepzar a escribir nuestro script. 
- Al querer guardar podemos hacerlo con `Ctrl + O` nos pedirá en la parte inferior un nombre para el archivo. 
- Luego podremos salir utilizando `Ctrl + X`
- Nos pedirá confirmar el nombre si aceptamos se sobreescribe, si le cambiamos el nombre creará otro archivo .py
- Nota: El scrit se guarda en el directorio actual en el que ejecutamos el comando `Nano`
- Para ver el contenido del Script podemos utilzar el comando `cat` seguido del nombre: Ejm: `cat hwllo_world.py`

### Ejecutar un script de python:
- En cmd/powersehl ejecutamos con python archivo.py 
- En linux podemos ejecutar así: 
    1.  python3 Archivo.py
    2. ./Archivo.py (Para que funcione previamente debemos abrir el script con `nano` y agregar al principio esta linea: `#!/usr/bin/env python`) adicionalmente cambiar los permisos para permitir ejecución usando **chmod** así : `chmod +x Archivo.py`



### Eliminación de un archivo de un directorio: 
Utilizamos el comando `rm` acompañado del nombre del archivo, podemos hacer `rm hello_world` (Se elimina si está en el directorio actual)

### Mover de un archivo de un directorio: 
Utilizamos el comando `mv` acompañado del nombre del archivo y la nueva ruta, podemos hacer:
 1. `mv hello_world.py` "/mnt/c/Users/DanielJaramilloBusta/Onedrive - XPERTGROUP S.A.S/XperGroup_Cursos Nueva Ruta"`

 2. `mv hello_word.py "nuva_ruta"`