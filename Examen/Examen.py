class PuestoDeTrabajo:
    def __init__(self, codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo
    def __str__(self):
        return f"{self.codigo} - {self.descripcion} ({self.areaSolicitante}) Plazas:{self.plazasRequeridas} S/{self.sueldo}"
    def __repr__(self):
        return f"{self.codigo} [{self.descripcion}] {self.areaSolicitante} S/{self.sueldo}"
 
lista = []
def buscaPuesto(lst, p) -> bool:
    for x in lst:
        if x.codigo == p.codigo or x.descripcion == p.descripcion or x.areaSolicitante == p.areaSolicitante:
            return True
    return False
 
def AgregaPuesto():
    codigo = int(input("Codigo: "))
    descripcion = input("Descripcion: ")
    areaSolicitante = input("Area Solicitante: ")
    plazasRequeridas = int(input("Plazas Requeridas: "))
    sueldo = float(input("Sueldo: "))
 
    if len(descripcion) < 3 or len(areaSolicitante) < 3:
        print("Error: strings deben tener al menos 3 letras."); return
    if codigo <= 0 or plazasRequeridas <= 0 or sueldo <= 0:
        print("Error: numericos deben ser mayor a cero."); return
 
    nuevo = PuestoDeTrabajo(codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo)
    if buscaPuesto(lista, nuevo):
        print("Error, ya existe."); return
 
    lista.append(nuevo)
    print("Puesto agregado")
 
def Mostrar():
    if not lista: print("Lista vacia."); return
    for p in lista: print(p)
def Burbuja(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j].codigo < lst[j+1].codigo:
                lst[j], lst[j+1] = lst[j+1], lst[j]
def BorrarPuesto():
    codigo = int(input("Codigo a borrar: "))
    Burbuja(lista)
    for i in range(len(lista)):
        if lista[i].codigo == codigo:
            lista.pop(i); print("Puesto eliminado."); return
    print("Codigo no encontrado.")
def ordInsercion(lst):
    for i in range(1, len(lst)):
        actual = lst[i]; j = i - 1
        while j >= 0 and lst[j].sueldo < actual.sueldo:
            lst[j+1] = lst[j]; j -= 1
        lst[j+1] = actual
def BuscarSueldo():
    ordInsercion(lista)
    sueldo_buscado = float(input("Sueldo a buscar: "))
    izq, der, id = 0, len(lista) - 1, -1
    while izq <= der:
        mid = (izq + der) // 2
        if lista[mid].sueldo == sueldo_buscado: id = mid; der = mid - 1
        elif lista[mid].sueldo > sueldo_buscado: izq = mid + 1
        else: der = mid - 1
    if id == -1: print("Sueldo no encontrado."); return
    while id < len(lista) and lista[id].sueldo == sueldo_buscado:
        print(lista[id]); id += 1
def ordSeleccion(lst):
    n = len(lst)
    for mano in range(n):
        posMayor = mano
        for ver in range(mano + 1, n):
            if lst[ver].plazasRequeridas * lst[ver].sueldo > lst[posMayor].plazasRequeridas * lst[posMayor].sueldo:
                posMayor = ver
        lst[mano], lst[posMayor] = lst[mano], lst[posMayor]
def PuestosAContratar():
    presupuesto = float(input("Presupuesto total: "))
    ordSeleccion(lista)
    acumulado = 0
    for p in lista:
        total = p.plazasRequeridas * p.sueldo
        if acumulado + total <= presupuesto:
            acumulado += total; print(p)
        else: break
    print(f"Total invertido: {acumulado}")
def menu():
    while True:
        print("\n1-Agregar 2-Mostrar 3-Borrar 4-BuscarSueldo 5-Contratar 6-Salir")
        op = input("Opcion: ")
        if op == "1": AgregaPuesto()
        elif op == "2": Mostrar()
        elif op == "3": BorrarPuesto()
        elif op == "4": BuscarSueldo()
        elif op == "5": PuestosAContratar()
        elif op == "6": break
        else: print("error, escoja otra opcion")
menu()