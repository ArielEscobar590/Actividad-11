def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


cantidad = int(input("¿Cuantos nombres desea ingresar?"))
nombres = []
for n in range(cantidad):
    name=input(f"Nombre {n+1}: ")
    nombres.append(name)

resultado = quick_sort(nombres)
print(resultado)