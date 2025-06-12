# Se utilizan rutas para guardar archivos y recuperarlos.
import os

#Directorio actual
current_directory = os.getcwd()

# cwd comando para archivos externos
def get_file_path(filename):
    """
    Obtiene la ruta completa del archivo dado su nombre.
    """
    return os.path.join(current_directory, filename)

outputs = {}
outputs["current_directory"] = current_directory
outputs["files_and_directories"] = os.listdir()
outputs["path_value"] = os.environ.get('PATH', '') # Modifica la variable PATH desde python.

#Supongamos una nueva ruta que queremos añadir a la variable PATH
new_path = get_file_path('new_directory')
os.environ['PATH'] = os.pathsep.join([os.environ['PATH'], new_path])
outputs["new_path"] = new_path

#El cambio será temporal, solo afectará al proceso actual de Python y no se guardará permanentemente en el sistema.

# Remover un archivo o directorio
def remove_file_or_directory(path):
    """
    Elimina un archivo o directorio dado su ruta.
    """
    if os.path.isfile(path):
        os.remove(path)
        return f"Archivo {path} eliminado."
    elif os.path.isdir(path):
        os.rmdir(path)
        return f"Directorio {path} eliminado."
    else:
        return f"{path} no es un archivo ni un directorio válido."
    
# Renombrar un archivo o directorio
def rename_file_or_directory(old_path, new_path):
    """
    Renombra un archivo o directorio de old_path a new_path.
    """
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        return f"{old_path} renombrado a {new_path}."
    else:
        return f"{old_path} no existe."
    

# Obtener el path padre de la ruta actual 
def get_parent_directory(path):
    """
    Obtiene el directorio padre de la ruta dada.
    """
    return os.path.dirname(path)

