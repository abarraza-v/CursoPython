# Si el módulo está fuera de la ruta

import sys

sys.path.append("c:\\xampp\\htdocs\\CursoPython\\modules_buenos")
print(sys.path)

import saludito  # Tira error al modificar el path, pero el programa funciona bien.

saludonuevo = saludito.saludar("ale")
print(saludonuevo)
