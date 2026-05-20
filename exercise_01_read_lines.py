def read_lines(filename):

    resultado = []

    with open(filename, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea != "":
                resultado.append(linea)

    return resultado
