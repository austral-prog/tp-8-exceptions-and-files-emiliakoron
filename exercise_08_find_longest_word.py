def find_longest_word(filename):

    with open(filename, "r") as archivo:

        contenido = archivo.read()

    palabras = contenido.split()

    if palabras == []:
        raise ValueError("file has no words")

    mayor = palabras[0]

    for palabra in palabras:

        if len(palabra) > len(mayor):
            mayor = palabra

    return mayor
