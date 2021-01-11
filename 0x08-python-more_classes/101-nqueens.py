#!/usr/bin/python3

from sys import argv, exit

if len(argv) == 2:
    number = argv[1]
    if (number.isdigit()):
        number = int(number)
        if number < 4:
            print("N must be at least 4") 
            exit(1)
    else:
        print("N must be a number")
        exit(1)

'''
1. Colocamos reina en 0,0
2. Colocamos siguiente reina en 1,0 (columna + 1)
3. Verificamos si esta bajo ataque en diagolaes, filas o columnas
4. Si es posible, confirmamos posicion y colocamos tercera reina y seguimos con el prodecimiento hasta que todas las reinas queden en espacios habilitados. Guardar lista con 
soluciones y proceder a mover primera reina en caso que sea posible.
5. Si no es posible (esta bajo ataque): Hay lugar en el tablero para mover la reina?
5.a Si hay -> Movemos segunda reina y vuelvo a verificar
5.b No hay -> La anterior reina se puede mover?
6.a No se puede mover -> No hay mas soluciones
6.b Se puede mover -> colocamos reina en nueva posicion y volvemos a realizar la verificaciones
'''

else:
    print("{} {}".format(argv[0],argv[1]))
    print("Usage: nqueens N
