# Alumno mayor es el profesor
# Alumno menor es el asistente
pedir_valor = lambda: int(input("¿Cuántos alumnos vinieron a clase hoy?  "))


def pasar_lista(cantidad_alumnos):
    lista_alumnos = list()

    for i in range(cantidad_alumnos):
        nombre = input(f"Ingrese el nombre del Alumno {i+1}  ")
        edad = int(input(f"Ingrese la edad del Alumno {i+1}  "))
        alumno = nombre, edad
        lista_alumnos.append(alumno)
    return lista_alumnos


def retornar_mayor(lista_alumnos):
    alumno_mayor = lista_alumnos[0]
    for alumno in lista_alumnos:
        if alumno[1] > alumno_mayor[1]:
            alumno_mayor = alumno
    return alumno_mayor


def retornar_menor(lista_alumnos):
    alumno_menor = lista_alumnos[0]
    for alumno in lista_alumnos:
        if alumno[1] < alumno_menor[1]:
            alumno_menor = alumno
    return alumno_menor


cantidad_alumnos = pedir_valor()
lista_alumnos = pasar_lista(cantidad_alumnos)
alumnomayor = retornar_mayor(lista_alumnos)[0]
alumnomenor = retornar_menor(lista_alumnos)[0]

print(f"El alumno mayor es {alumnomayor}, así que será el profesor")
print(f"El alumno menor es {alumnomenor}, así que será el ayudante")
