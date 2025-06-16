#!/usr/bin/env python3

import re 

def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        print("Agregando linea")
        print("Agregando linea")
        return result
    return "{} {}".format(result[2], result[1])