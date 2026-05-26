def recx(lst, PI, PF):
    if PI > PF:
        return 0
    return lst[PI - 1] + recx(lst, PI + 1, PF)
 
n = int(input("Ingrese el amaño de la lista: "))
lst = []
for i in range(n):
    lst.append(int(input(f"Elemento {i + 1}: ")))
 
PI = int(input("PRIMERA POSICION (PI): "))
PF = int(input("ULTIMA POSICION (PF): "))
 
print(f"Resultado = {recx(lst, PI, PF)}")
 