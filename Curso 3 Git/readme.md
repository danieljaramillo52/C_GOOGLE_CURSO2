# Curso 3: git hub. (Sistemas de control de versiones)


## Diferencia entre artchivos comando diff. 

Evidencia diferencias en el codigo usando el sistema operativo: 

Spungamos dos archivos.  **rearrange1.py** y  **rearrange2.py** y queremos ver las diferencias entre los mismos. 

Podemos usar cat para ver ambos desde (Ubuntu)
- cat rearrange1.py
- cat rearrange2.py

Obtenemos: 

```python
#!/usr/bin/env python3

import re 

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result == None:
        return result
    return "{} {}".format(result[2], result[1])
```

 y 

```python
#!/usr/bin/env python3

import re 

def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        return result
    return "{} {}".format(result[2], result[1])
```

En apariencia similares. 

Podemos usar el comando **diff rearrange1.py rearrange2.py**

<     result = re.search(r"^([\w .]*), ([\w .]*)$", name)
---
>     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)

Podemos ver que : < Significa que se elimino esta linea y fue reemplazada por lo que encontramos aquí >

Podemos utilizar **diff -u diff rearrange1.py rearrange2.py**

Y nos entrega algo mejor mas detallado mostrando que linea se agregó con (+) y cual se sustrajo con (-)

Modificando `rearrange2.py` al usar **diff -u** podemos ver
```python
import re 

def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        print("Agregando linea")
        print("Agregando linea")
        return result
    return "{} {}".format(result[2], result[1]) 
```

En esencia veremos sobre cada linea agregada o quitada estos simbolos (+) y (-)

Ejecutamos: 

**diff -u rearrange1.py rearrange2.py**

"**`-`**    result = re.search(r"^([\w .]*), ([\w .]*)$", name)"

"**`+`**   result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)"

"**`+`**  print("Agregando linea")"

"**`+`**  print("Agregando linea")"


### Comando adicional wdif

Mostrara sola la linea el cambio encerrado en llaves. 


## Comando patch

(Para poder ejecutar las intrucciones borrar rearrange3.py y volverlo a crear desde una copia de rearrange1.py)

Aplica las diferencias de un archivo a otro. Para temas de correciones. 

Poe ejemplo supongamos **rearrange3** copia de **rarrange1** con este vamos a transformarlo usando los cambios de **rearrange2.py**



#### Lo hacemos así: 

1. Creamos un archivo parche para el archivo que vamos a modificar. 

**``diff -u rearrange1.py rearrange2.py > cambios.patch``**

En este caos estamos guardando en el archivo cambios.path que nos guardará los cambios entre ``rearrange1.py``  y ``rearrange2.py``  


Notemos que se genera el archivo en cuestión: **cambios.patch** 

Agora podemos pasar estos cambios al archivo rearrange3.py usando: 

**``patch rearrange3.py < cambios.patch``**

Estamos aplicando los cambios que hay en rearrange2 a rearrange3 

recibimos la salida: **patching file rearrange3.py** y al revisar nuevamente rearrange3.py 

Podemos ver que ahora rearrange2 y rearrange3 son iguales. 
