with open("Apuntes\\Archivos\\texto.txt", "w", encoding="UTF-8") as archivo:
    # Sobreescribiendo el archivo (Se elimina el contenido previamente añadido).
    # archivo.write("He añadido esta linea con python!")

    # Sobreescribir 2 lineas con writelines(). (Es iterable)
    archivo.writelines(
        ["Hola, esta linea se añadido con writelines\n", "Aún no lo entiendo la verdad"]
    )
