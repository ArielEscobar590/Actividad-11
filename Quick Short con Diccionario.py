def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[carnet]
    menores = [x for x in lista[carnet][1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[carnet][1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

estudiantes = {}
cantidad = int(input("¿Cuántos estudiantes desea ingresar? "))

for i in range(cantidad):
    print(f"\nEstudiante #{i + 1}")
    carnet = input("Ingrese el número de carnet: ")
    nombre = input("Ingrese el nombre completo: ")
    edad = int(input("Ingrese la edad: "))
    carrera = input("Ingrese la carrera: ")
    correo = input("Ingrese el correo electrónico: ")
    telefono = input("Ingrese el número de teléfono: ")

    estudiantes[carnet] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "contacto": {
            "correo": correo,
            "telefono": telefono
        }
    }

resultado = quick_sort(estudiantes)
print(resultado)