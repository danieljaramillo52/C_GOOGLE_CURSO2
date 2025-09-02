# Guía rápida: varias claves SSH en un mismo equipo para múltiples cuentas de GitHub

> **Objetivo:** usar **una llave SSH por cuenta** (personal, trabajo, etc.) en el **mismo PC**, sin mezclarlas.

---

## 0) Requisitos
- Git (incluye **OpenSSH**) y/o **OpenSSH Client** en Windows.
- Terminal: **PowerShell** (Windows) o **Git Bash**.
- Tu usuario de GitHub (ej.: `danieljaramillo52`) y, si aplica, el de trabajo/organización.

---

## 1) Generar una **llave por cuenta**
> Cambia los nombres de archivo (`-f`) y los comentarios (`-C`) a tus datos.

**Git Bash o PowerShell**

```bash
# Cuenta personal
ssh-keygen -t ed25519 -C "tu_email_personal" -f ~/.ssh/id_ed25519_github_personal

# Cuenta de trabajo
ssh-keygen -t ed25519 -C "tu_email_trabajo" -f ~/.ssh/id_ed25519_github_work
```

Se crean pares **privada** (`~/.ssh/id_ed25519_github_*`) y **pública** (`~/.ssh/id_ed25519_github_*.pub`).  
> ⚠️ **Nunca** compartas ni subas a repos la **privada** (la que **no** termina en `.pub`).

---

## 2) Cargar llaves en el **ssh-agent**

### PowerShell (Windows)
```powershell
Start-Service ssh-agent
Set-Service -Name ssh-agent -StartupType Automatic

ssh-add "$env:USERPROFILE\.ssh\id_ed25519_github_personal"
ssh-add "$env:USERPROFILE\.ssh\id_ed25519_github_work"

ssh-add -l   # listar llaves cargadas
```

### Git Bash
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_github_personal
ssh-add ~/.ssh/id_ed25519_github_work

ssh-add -l   # listar llaves cargadas
```

---

## 3) Configurar `~/.ssh/config` con **aliases**

> Esto fuerza a que cada alias use **su** llave.

```
# ~/.ssh/config
Host github.com-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_github_personal
  IdentitiesOnly yes
  AddKeysToAgent yes

Host github.com-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_github_work
  IdentitiesOnly yes
  AddKeysToAgent yes
```

> En Windows, las rutas con `~` funcionan; si prefieres absolutas:  
> `IdentityFile C:/Users/TU_USUARIO/.ssh/id_ed25519_github_personal`

---

## 4) Subir **cada clave pública** a su cuenta de GitHub

1. Copia el contenido de la **pública** al portapapeles:
   - PowerShell:  
     ```powershell
     Get-Content "$env:USERPROFILE\.ssh\id_ed25519_github_personal.pub" | Set-Clipboard
     ```
   - Git Bash:  
     ```bash
     clip < ~/.ssh/id_ed25519_github_personal.pub
     ```
2. GitHub → **Settings** → **SSH and GPG keys** → **New SSH key** → pega y guarda.  
3. Repite con la key de **trabajo** en la **otra cuenta**.

---

## 5) Probar y usar los aliases en tus repos

**Probar conexión** (usa los aliases definidos en `~/.ssh/config`):
```bash
ssh -T git@github.com-personal
ssh -T git@github.com-work
```

**Cambiar la URL remota de un repo existente**:
```bash
# Repo personal
git remote set-url origin git@github.com-personal:TU_USUARIO/repo.git

# Repo de trabajo
git remote set-url origin git@github.com-work:ORG_O_EMPRESA/repo.git
```

**Clonar directamente con alias**:
```bash
git clone git@github.com-personal:TU_USUARIO/mi-repo-personal.git
git clone git@github.com-work:ORG_O_EMPRESA/mi-repo-work.git
```

> La **primera vez** que te conectes por SSH, te pedirá **confirmar la huella** de `github.com`; acepta si coincide con la oficial.  
> Quedará guardada en `~/.ssh/known_hosts` y no volverá a preguntar.

---

## 6) Identidad de **commits** por carpeta (opcional, recomendado)

**~/.gitconfig** (global):
```
[includeIf "gitdir:~/repos/work/"]
  path = ~/.gitconfig-work
[includeIf "gitdir:~/repos/personal/"]
  path = ~/.gitconfig-personal
```

**~/.gitconfig-work**:
```
[user]
  name = TU_NOMBRE
  email = tu_email_trabajo
```

**~/.gitconfig-personal**:
```
[user]
  name = TU_NOMBRE
  email = tu_email_personal
```

> Coloca tus repos en `~/repos/work/` y `~/repos/personal/` (o rutas equivalentes).

---

## 7) Solución de problemas rápidos

- **“Too many authentication failures”** → asegúrate de `IdentitiesOnly yes` en `~/.ssh/config` y que el `ssh-agent` solo tenga las llaves necesarias (`ssh-add -D` para vaciar y volver a cargar).  
- **Para ver qué llave usa**:  
  ```bash
  GIT_SSH_COMMAND="ssh -v" git ls-remote origin
  ```
- **Cambiar/rotar una llave**: borra en GitHub la anterior, elimina del `ssh-agent` (`ssh-add -d RUTA`), genera una nueva y repite los pasos.  
- **Permisos (Unix)**: `~/.ssh` = 700, privada = 600, pública = 644 (en Windows normalmente no hace falta ajustarlos).

---

## 8) Seguridad esencial
- **Nunca** subas la **clave privada** (`id_ed25519_*` sin `.pub`) a ningún repositorio.
- Usa **passphrase** al generar la llave y confía en el **ssh-agent** para no reescribirla todo el tiempo.
- Haz **backup seguro** de tus claves privadas (cifrado, gestor de contraseñas con archivos adjuntos, etc.).

---

### Anexo: ejemplos con tu ruta de Windows
```powershell
# Cargar claves en PowerShell (Windows)
ssh-add "C:\Users\DanielJaramilloBusta\.ssh\id_ed25519_github_personal"
ssh-add "C:\Users\DanielJaramilloBusta\.ssh\id_ed25519_github_work"
```

```text
# ~/.ssh/config (Windows) con rutas absolutas estilo POSIX
Host github.com-personal
  HostName github.com
  User git
  IdentityFile C:/Users/DanielJaramilloBusta/.ssh/id_ed25519_github_personal
  IdentitiesOnly yes

Host github.com-work
  HostName github.com
  User git
  IdentityFile C:/Users/DanielJaramilloBusta/.ssh/id_ed25519_github_work
  IdentitiesOnly yes
```
