#!/usr/bin/python3
def best_score(a_dictionary):
    maximo = 0
    llave = ""
    if a_dictionary is not None:
        for clave, valor in a_dictionary.items():
            if valor > maximo:
                llave = clave
                maximo = valor
        return llave
    else:
        return None
