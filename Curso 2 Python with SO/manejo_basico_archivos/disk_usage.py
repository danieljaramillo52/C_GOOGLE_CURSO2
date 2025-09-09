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
    # Aquí podrías añadir más lógica si es necesario
    # Por ejemplo, podrías llamar a otras funciones o realizar otras comprobaciones
    