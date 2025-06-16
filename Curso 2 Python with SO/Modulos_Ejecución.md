### Creación y ejecución de modulos. 

1. Creamos un scrip de nano en la ruta actual utilizando **nano** escribimos el scirpt.

Modulo **Areas.py**

```python
#!/usr/bin/env python`
import math

def triangle(base,height):
	return base * height / 2


def rectangule(base, height):
        return base * height

def circle(radious):
        return math.pi * (radious**2)
```

2. Podremos usarlo ingresando a **python3** e importandolo: 

-  python3 
-  `import Areas` (No es necesario especificar el .py)

(Cuidado con la ruta del directorio actual: debe contener el archivo **Areas.py**)

3. Usamos su contenido: Areas.triangle(3,5) 

Por convencvión los scritps/Modulos empezarán con una letra minuscula. 


### Editor de codigo opciones: 

1. Editor **`vim`**

2. Editor atom **`atom`**

3. Abrir editor de código **code** puede instalar el visual studio code / Si tiene el acceso. (Desde power shell podrias ejecutarlo )

Para desplegarlos escribimos la palabra clave respectivamente. 

Si ya tneemos un script podemos simplemente usar 
`vim Areas.py` ó `atom Areas.py` para ejecutarlo. 

Salir de los editores:
 1. ``vim``: Escribimos **:q** para salir ( Presionamos la tecla **i** para insertar mas codigo)
 podemos usar :wq para guardar los cambios
 :w nombre_del_archivo para añadirle un nombre
 2. ``atom``: presionamos **Ctrl+ Q** ( Descontinuado desde 2022)


#### Ejemplo automatización parámetros de disco.

Dentro de python

1. Utilización modulo `shutil`
        - import shutil
        - du = shuil.disk_usage("/")
        - Porcentaje = du.free / du.total * 100 ( Porcentaje libre de uso del disco)


Vamos a escribir un script que realice todo esto. 

```python
#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage():
    """Permite obtener el uso del disco."""
    du = shutil.disk_usage('/')
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    """ Permite comprobar el uso de la CPU."""
    usage = psutil.cpu_percent(interval=1)
    return usage < 75

if not check_cpu_usage() or not check_disk_usage():
    print("ERROR!")
else:
    print("Everything is OK!")
```

## Vamos ahora a concederle permisos de ejecución  dentro de nuestor sistema

Usamos : **chmod +x nombre_archivo**




                                                                                                                                                                                                 