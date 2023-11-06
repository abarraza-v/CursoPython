# Guardando datos a trabajar

otros_cursos_max = 7
otros_cursos_min = 2.5

crudo_otros_cursos = 5
crudo_dalto = 3.5

otros_cursos_promedio = 4
curso_dalto = 1.5

# Porcentaje Inservible eliminado

porcentaje_inservible_eliminado_otros_cursos = (
    100 - otros_cursos_promedio * 100 / crudo_otros_cursos
)

porcentaje_inservible_eliminado_curso_dalto = round(
    100 - curso_dalto * 100 / crudo_dalto, 2
)

horas_vistas = 10

# Diferencias de duración

diferencia_con_min = 100 - curso_dalto / otros_cursos_min * 100
diferencia_con_max = 100 - curso_dalto * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - curso_dalto / otros_cursos_promedio * 100


print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el curso más rápido")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el curso más lento")
print(
    f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio de tiempo de otros cursos"
)
print("---------------------------------")

print(
    f"Otros cursos eliminan un {porcentaje_inservible_eliminado_otros_cursos}% del contenido inservible"
)
print(
    f"El curso de dalto elimina un {porcentaje_inservible_eliminado_curso_dalto}% del contenido inservible"
)
print("---------------------------------")

print(
    f"Si ves {horas_vistas} horas de el curso de dalto, es como ver {otros_cursos_promedio * 100 // curso_dalto / 10} de otros cursos en promedio"
)
print(
    f"Y si ves {horas_vistas} horas de otros cursos, sería equivalente a que te hubieras visto {curso_dalto * 100 // otros_cursos_promedio / 10} horas de el curso de dalto"
)
