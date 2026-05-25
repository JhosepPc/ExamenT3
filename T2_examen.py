import random
 #a=arreglo
 #i=indice

def recx(a, i, maximo, minimo):
    if i == len(a):
        return (maximo + minimo) / 2
    if a[i] % 3 == 0:
        if a[i] > maximo:
            maximo = a[i]
        if a[i] < minimo:
            minimo = a[i]
    return recx(a, i + 1, maximo, minimo)

n = int(input("Ingrese el tamaño del arreglo: "))
a = []
for i in range(n):
    a.append(random.randint(10, 9999))
 
print(a)
 
primero = 0
for x in a:
    if x % 3 == 0:
        primero = x
        break
 
print(f"Resultado = {recx(a, 0, primero, primero)}")