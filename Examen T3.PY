def imprimir(mat):
    for f in mat:
        print(f)
    print()
 
def validar(lab, f, c, res, vidas):
    if f < 0 or f >= len(lab) or c < 0 or c >= len(lab[0]):
        return False
    if lab[f][c] == 0 or res[f][c] == 1:
        return False
    if vidas <= 0:
        return False
    return True
 
def laberinto(lab, res, f, c, fin_f, fin_c, vidas):
    if f == fin_f and c == fin_c:
        res[f][c] = 1
        imprimir(res)
        return True
 
    if validar(lab, f, c, res, vidas):
        res[f][c] = 1
        imprimir(res)
 
        vida = vidas + lab[f][c] if lab[f][c] < 0 else vidas
 
        if laberinto(lab, res, f+1, c, fin_f, fin_c,vida): #Abajo
            return True
        elif laberinto(lab, res, f, c+1, fin_f, fin_c,vida): #Derecha
            return True
        elif laberinto(lab, res, f-1, c, fin_f, fin_c, vida): #Arriba
            return True
        elif laberinto(lab, res, f, c-1, fin_f, fin_c,vida): #Izquierda
            return True
        else:
            res[f][c] = 0
            imprimir(res)
            return False
    else:
        return False
 
lab = [
    [1,  1,  1,  1,  0,  1,  1,  1,  1],
    [-2, 0,  0, -1,  0,  1,  0,  1,  0],
    [1,  1,  0,  1,  1,  1,  0,  1,  0],
    [0,  1,  0, -1,  0,  0,  0, -1,  0],
    [1,  1,  1,  1,  1,  1,  1,  1,  0],
    [-1, 0,  0,  0,  0,  0,  0,  1,  1],
    [1,  1,  1,  1, -1,  1,  1,  1,  0],
    [1,  0,  0,  1,  0,  1,  0,  1,  0],
    [1,  1, -1,  1,  1,  1,  0,  1,  1],
]
 
print("laberinto original:")
imprimir(lab)
 
res = [[0 for _ in range(9)] for _ in range(9)]
 
if laberinto(lab, res, 8, 0, 0, 0, 3):
    print("¡Se logro escapar!")
else:
    print("no se encontro salida")