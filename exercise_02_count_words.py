def count_words(filename):

    palabras = {}

    with open(filename, "r") as archivo:

        for linea in archivo:

            lista = linea.lower().split()

            for palabra in lista:

                if palabra in palabras:
                    palabras[palabra] += 1
                else:
                    palabras[palabra] = 1

    return palabras
