
# Guía de estudio: Git

**Estado:** Traducido automáticamente del Inglés  
**Información:** Este elemento incluye contenido que aún no se tradujo a tu idioma preferido. .

---

En cualquier proyecto Git, hay tres secciones: el **directorio Git**, el **árbol de trabajo** y el **área de preparación**.  
Esta guía de estudio proporciona algunos conceptos básicos y comandos que pueden ayudarte a empezar con Git, así como directrices para ayudarte a escribir un mensaje de confirmación efectivo.

---

## Comando `git config`

El comando `git config` se utiliza para establecer los valores que identifican quién ha realizado cambios en los repositorios Git. Para establecer los valores de `user.email` y `user.name` a tu email y nombre, escribe:

```bash
$ git config --global user.email "me@example.com"
$ git config --global user.name "Mi nombre"
```

---

## Comando `git init`

```bash
~/checks$ git init
```

Crea un nuevo repositorio vacío en un directorio actual o reinicializa uno existente.

---

## Comando `ls -la`

```bash
~/checks$ ls -la
```

Comprueba la existencia de un directorio identificado.

```bash
~/checks$ ls -l .git/
```

Comprueba el contenido del directorio `.git/`, que es la base de datos para tu proyecto Git. Allí se almacenan los cambios y el historial de cambios.

---

## Comando `git add`

```bash
~/checks$ git add uso_disco.py
```

Permite a Git rastrear tu archivo y usarlo como parámetro al añadirlo al área de preparación (**staging area**).

---

## Comando `git status`

```bash
~/checks$ git status
```

Se utiliza para obtener información sobre el árbol de trabajo actual y los cambios pendientes.

---

## Comando `git commit`

```bash
~/checks$ git commit
```

Ejecuta la confirmación de cambios desde el área de preparación al directorio `.git`. Se abre un editor de texto para introducir un mensaje de confirmación.

---

## Pautas para escribir mensajes de confirmación

Un mensaje de confirmación se divide en dos secciones: **resumen** y **descripción**.

- **Resumen**: Primera línea de hasta 50 caracteres, como una cabecera.
- **Descripción**: Segunda sección de hasta 72 caracteres por línea, más detallada. Puede incluir referencias a errores, soluciones o enlaces.

🔗 Ejemplo de estilo de mensaje de confirmación: [commit.style](https://commit.style/)

---

## Puntos clave

Conocer los comandos básicos de Git y cómo escribir buenos mensajes de confirmación puede ayudarte a:
- Empezar a usar Git eficientemente.
- Comunicarte mejor con tus colaboradores.
