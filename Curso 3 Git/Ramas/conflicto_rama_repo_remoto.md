## Conflicto rama repositorio remoto. 

Supongamos que tenemos un repositorio y un colaborador. Un  colaborador tiene otra rama, **y quiere unir cambios con los que tenemos en la rama main**, a esta rama ya le hemos realizado cambios... Por lo que se profuce un conflicto para unir con la rama **``main``**. 

### **Ejemplo**


1. **Creamos una nueva rama**

```bash
git branch new_feature # Creamos

git switch new_feature #Cambiamos a ella

git branch # Consultamos por las ramas disponibles. 

PS C:\Users\(...)\Cursos 2-7> git branch 
  main
* new_feature
```

2. Podemos crear un archivo para generar un conflicto 

Así está en la rama creada **``"new_feature"``**`

```python
def main():
        """El método main encapsula el procedimiento de lógica del proyecto y lo lanza"""
        print("Todo está Ok!")

main()

def suma_elementos(elemento1: int, elemento2: int):
        """Suma dos elementos 

        Args:
            elemento1 (int): primer elemento a sumar 
            elemento2 (int): segundo elemento a sumar
        """
        return elemento1 + elemento2
```

Confirmamos cambios con **``git add``** y **``git commit``** en la rama adicional y procedemos a subir esta nueva rama al repositorio remoto. 


```bash

PS C:\Users\(...)\Cursos 2-7> git branch 
  main
* new_feature

PS C:\Users\(...)\Cursos 2-7> git add . 

PS C:\Users\(...)\Cursos 2-7> git commit -m "Archivo free_memory modificado en la nueva rama a subir 'new_feature'"
[new_feature 23b0918] Archivo free_memory modificado en la nueva rama a subir 'new_feature'
 3 files changed, 100 insertions(+), 1 deletion(-)
 create mode 100644 Curso 3 Git/Ramas/conflicto_rama_repo_remoto.md

PS C:\Users\(...)\Cursos 2-7> git push -u origin new_feature
Enumerating objects: 19, done.
Counting objects: 100% (19/19), done.
Delta compression using up to 12 threads
Compressing objects: 100% (13/13), done.
Writing objects: 100% (13/13), 2.81 KiB | 479.00 KiB/s, done.
Total 13 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6), completed with 3 local objects.
remote: 
remote: Create a pull request for 'new_feature' on GitHub by visiting:
remote:      https://github.com/danieljaramillo52/C_GOOGLE_CURSO2/pull/new/new_feature
remote:
To https://github.com/danieljaramillo52/C_GOOGLE_CURSO2.git
 * [new branch]      new_feature -> new_feature
branch 'new_feature' set up to track 'origin/new_feature'.
PS C:\Users\(...)\Cursos 2-7>
```

Podememos ver en fecto la rama agregada al repo remoto. 

![Nueva_rama_repo_remoto](nueva_rama_repo_remoto.png)

Ahora nuestro colaborador, realizo cambios en la rama **``main``** a la función que teniamos en uno de nuestros modulos. 


```python
def main():
        """El método main encapsula el procedimiento de lógica del proyecto y lo lanza"""
        print("Todo está Ok!")

main()

def suma_elementos(num1: int, num2: int):
        """Suma dos elementos 

        Args:
            num1 (int): primer elemento a sumar 
            num2 (int): segundo número  a sumar
        """
        return elemento1 + elemento2

```

Luego de consginar cambios, podemos ver que no estamos del todo sincronizadso entre ramas. 

git switch main
Switched to branch 'main'
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

las ramas divergen porque el cambio realizado en el main "**main**" por el colaborador no está en mi rama **main** y yo tengo un cambio en la rama remota. 

Vamos a intentar traer los cambios del repo remoto primero: 

## Al intentar fusionar las ramas: 

```bash
git merge main
Auto-merging Curso 3 Git/Ramas/conflicto_rama_repo_remoto.md
CONFLICT (add/add): Merge conflict in Curso 3 Git/Ramas/conflicto_rama_repo_remoto.md
Auto-merging free_memory.py
CONFLICT (content): Merge conflict in free_memory.py
Automatic merge failed; fix conflicts and then commit the result.
``` 

Por lo que debemos resovler el conflicto para que el merge siga adelante. 

# Git fetch

Descarga los cambios del repostorio remoto, pero no los combina con el repositorio actual, por lo tanto **NO** genera conflictos. Solo descarga la información. 

# Git rebase 

Ya sabemos que aplana el historial toma la rama original

A---B---C Del remoto. 
     
     D--E

Y los "reaplica" sobre "C"

A--B--C--D'--E'

**¿Cuando usar git rebase?**
Mantener un historial lineal.

Estas colaborando y ya compartiste los cambios

Antes de hacer ``push`` para limpiar tu historial. 

### No usar **rebase**

En ramas compartidas si ya hicistew push, a menos que todos estén cordinados. Puede causar conflictos al forzar el historial. 

(Vamos a intentarlo)

```git rebase origin/main```

Se abrirá el editor de VSCode para solucionar el conflicto en cuestión. Posteriormente deberemos continuar el rebase. 

```git rebase --continue```

✅ ¿Qué pasó?
Ejecutaste git rebase origin/main

Git:

Descargó los commits de origin/main

"Reescribió" tus commits locales para aplicarlos encima del historial remoto

Posiblemente tuviste conflictos → los resolviste

Al terminar, tu rama ahora tiene un historial lineal y actualizado con los cambios del remoto.

📌 Antes del rebase:

origin/main: A---B---C
tu rama:             \---D---E

📌 Después del rebase:

tu rama (actual): A---B---C---D'---E'

Tus commits (D y E) fueron reaplicados encima de origin/main, con nuevos IDs (D', E').

🎯 ¿Qué debes hacer ahora?

🔁 Si ya habías hecho git push antes del rebase:
Ahora el historial de tu rama ha cambiado. Entonces, para actualizar el remoto, debes forzar el push:

```bash
git push --force
```
⚠️ Esto sobreescribe el historial remoto con tu nuevo historial reescrito.

✅ Si aún no habías hecho push:
Solo haz:

```bash
git push
```
Y no necesitas forzar nada.


### Cambio en la configuración de git para evitar ramas "Rosadas" (Por conflictos de merge.)

La configuación por defecto de un ``git pull`` es: 

```bash
git fetch
git merge origin/main
```

Por lo tanto fuerza directamente los cambios hasta que encuentra un conflicto. 

Luego nos pone a resolverlo. Una vez resuelto genera una rama divergente. 

![Imagen rama_diverente NO CREADA](/Curso%203%20Git/Ramas/Rama_divergente_NO_CREADA.png)


Podemos sin embargo **``Cambiar esta configuración, así evitamos que se creen estas ramas adicionales``**

Utilizamos: 

```bash
git config --global pull.rebase true
```

### 🧠 Entonces, ¿qué logras con esto?

✅ 1. Conflictos igual se detectan — pero uno por uno

Cuando haces pull con rebase, Git aplica tus commits uno por uno sobre origin/main.

Si hay un conflicto en uno de ellos, Git lo pausa inmediatamente y te deja resolverlo.

Luego continúas con:

```bash
git rebase --continue
```

🔁 Esto no cambia tu momento actual en la historia del proyecto, solo te hace reordenar tus cambios como si hubieran venido después.

### ❌ ¿Qué evita esto?

1. Evita un commit de merge automático y feo.

2. Evita una desviación visual en el historial (como la rama rosada)

3. No crea ramas paralelas innecesarias.


# Nuevo procedimiento: 


```bash
on\C_GOOGLE_CURSOS> git fetch
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 323 bytes | 26.00 KiB/s, done.
From https://github.com/danieljaramillo52/C_GOOGLE_CURSO2
   6d2ccfc..5332814  main       -> origin/main
```
Primero el fetch.

```bash
PS C:\Users\ovejo\Documents\Xpert-group\Cursos XpertGroup\Certificacion GOOGLE automatizacion python\C_GOOGLE_CURSOS> git rebase origin/main
Auto-merging free_memory.py
CONFLICT (content): Merge conflict in free_memory.py
error: could not apply 98a5c10... Cambio comiteado solo para generar un conflicto
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 98a5c10... Cambio comiteado solo para generar un conflicto
```

**git rebase origin/main** Luego este el conflicto por tener un commit en local que genera conflicto con lo traido del remoto.

```bash
PS C:\Users\ovejo\Documents\Xpert-group\Cursos XpertGroup\Certificacion GOOGLE automatizacion python\C_GOOGLE_CURSOS> git rebase --continue 
```

Posterior a su solución continuamos con el rebase


Notemos que al hacer un **git pull** es más seguro cuando sabemos que iniciamos nuestro proceso de trabajo. Ahora con la configuración de rebase podemos resolver las cosas, decidir, hacer un commit y lanzar la definitva al repo remoto 


##### **continuamos con el rebase**

Luego de esto debemos hacer un commit y luego un push para actualizar el rémoto. 

Notemos: 

![Solucion de conflictos sin ramas innecesarias](/Curso%203%20Git/Ramas/sol_conflict_sin_ramas_innecesarias.png)