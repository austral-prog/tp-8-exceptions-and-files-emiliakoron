def read_sales(filename):

    ventas = {}

    with open(filename, "r") as archivo:

        contenido = archivo.read()

    registros = contenido.split(";")

    for registro in registros:

        if registro != "":

            producto, valor = registro.split(":")

            valor = float(valor)

            if producto not in ventas:
                ventas[producto] = []

            ventas[producto].append(valor)

    return ventas
