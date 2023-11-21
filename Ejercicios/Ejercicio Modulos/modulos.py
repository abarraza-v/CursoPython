# Al importar de esta forma, estamos creando un objeto módulo, que tendrá como métodos
# las funciones dentro de él.
import modules.modulo_saludar as m_saludar

# Importando funciones específicas
from modules.modulo_saludar import saludar, saludo_raro

saludo = m_saludar.saludar("Alejandrito")
saludo_weird = saludo_raro("Ale")

print(saludo)
print(saludo_weird)

# Para ver las propiedades y métodos del objeto módulo
# print(dir(m_saludar))

# Accedemos al nombre de este módulo
# print(__name__)

# Accedemos al nombre del módulo llamado
# print(m_saludar.__name__)

print(type(saludar))
