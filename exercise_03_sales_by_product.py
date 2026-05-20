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


def process_sales(data):

    for producto in data:

        ventas = data[producto]

        total = sum(ventas)

        promedio = total / len(ventas)

        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
