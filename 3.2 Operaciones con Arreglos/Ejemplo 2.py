# Ejercicio 2 matriz 3x3
matriz = [
    [8,13,9],
    [2,10,4],
    [6,8,3]
]
print(matriz)
# Metodo de ordenamiento buble_sort
def buble_sort(fila):
    #algoritmo buble_sort
    n=len(fila)
    for i in range(n):
        for j in range(n-1,i,-1):
            if fila[j]>fila[j-1]:
                fila[j],fila[j-1]=fila[j-1],fila[j]
                print(fila)
print("matriz original")
print(matriz)
buble_sort(matriz[0])
print(matriz)