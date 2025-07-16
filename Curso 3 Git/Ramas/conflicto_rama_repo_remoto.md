## Conflicto rama repositorio remoto. 

Supongamos que tenemos un repositorio y un colaborador. Un  colaborador tiene otra rama, **y quiere unir cambios con los que tenemos en la rama main**, a esta rama ya le hemos realizado cambios... Por lo que se profuce un conflicto para unir con la rama **``main``**. 

### **Ejemplo**


1. **Creamos una nueva rama**

```bash
git branch new_feature # Creamos

git switch new_feature #Cambiamos a ella

git branch # Consultamos por las ramas disponibles. 

PS C:\Users\DanielJaramilloBusta\OneDrive - XPERTGROUP S.A.S\Xpert Group Cursos\Certificación Google_automatización_python\Cursos 2-7> git branch 
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