#!/usr/bin/python3
def best_score(a_dictionary):
    maximo = 0
    llave = ""
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        for clave, valor in a_dictionary.items():
            if valor > maximo:
                llave = clave
                maximo = valor
        return llave
