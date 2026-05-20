def csv_to_dict(filename):

    resultado = []

    with open(filename, "r") as archivo:

        lineas = archivo.readlines()

    if len(lineas) <= 1:
        return []

    headers = lineas[0].strip().split(",")

    for linea in lineas[1:]:

        datos = linea.strip().split(",")

        persona = {
            "name": datos[0],
            "age": int(datos[1]),
            "city": datos[2]
        }

        resultado.append(persona)

    return resultado
