# Matriz de 3x3
from types import new_class

matriz = [
    [8,13,9],
    [2,10,4],
    [6,8,3]
]
print(matriz)
#Funcion buscar_valor especifico

def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j]== valor_buscado:
                return i,j
valor_buscado=13
print(buscar_valor(matriz,valor_buscado))
if valor_buscado==valor_buscado:
    print("valor encontrado en la posicion",buscar_valor(matriz,valor_buscado))
else:
    print("Valor incorrecto")