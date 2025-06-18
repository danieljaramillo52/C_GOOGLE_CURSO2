
# Guía de estudio: Ramas y fusiones en Git

_Estado: Traducido automáticamente del Inglés_

Ahora que has aprendido acerca de las ramas y la fusión, utiliza esta guía de estudio como una referencia fácil para la creación de ramas en Git. Esta guía ofrece una breve explicación de estos útiles comandos junto con un enlace a la documentación de Git para cada comando.

> Mantener guías como ésta fácilmente accesibles puede ayudarte a programar más eficientemente.

---

## Comandos de Git para ramas y fusiones

### `git branch`

```bash
git branch
```
Lista, crea o borra ramas.

### `git branch <nombre>`

```bash
git branch <nombre>
```
Crea una nueva rama en tu repositorio.

### `git branch -d <nombre>`

```bash
git branch -d <nombre>
```
Elimina una rama (solo si ha sido fusionada).

### `git branch -D <nombre>`

```bash
git branch -D <nombre>
```
Fuerza la eliminación de una rama (aunque no haya sido fusionada).

### `git checkout <branch>`

```bash
git checkout <branch>
```
Cambia a otra rama existente.

### `git checkout -b <nueva-rama>`

```bash
git checkout -b <nueva-rama>
```
Crea una nueva rama y cambia a ella.

### `git merge <rama>`

```bash
git merge <branch>
```
Fusiona los cambios de una rama en la rama actual.

### `git merge --abort`

```bash
git merge --abort
```
Cancela una fusión en caso de conflicto, intentando volver al estado anterior.

### `git log --graph`

```bash
git log --graph
```
Muestra un gráfico ASCII del historial de commits y fusiones.

### `git log --oneline`

```bash
git log --oneline
```
Muestra el historial de commits en una sola línea por entrada.

---

### 📚 Enlace útil:
[Documentación oficial de Git](https://git-scm.com/doc)
