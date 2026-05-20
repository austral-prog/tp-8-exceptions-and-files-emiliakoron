def grades_stats(filename):

    resultado = {}

    with open(filename, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea != "":

                nombre, notas = linea.split(":")

                notas_lista = notas.split(",")

                numeros = []

                for nota in notas_lista:
                    numeros.append(float(nota))

                promedio = sum(numeros) / len(numeros)

                resultado[nombre] = (
                    promedio,
                    max(numeros),
                    min(numeros)
                )

    return resultado
