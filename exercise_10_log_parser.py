def parse_log(filename):

    logs = {}

    with open(filename, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea == "":
                continue

            if ":" not in linea:
                raise ValueError("invalid log line")

            nivel, mensaje = linea.split(":", 1)

            nivel = nivel.strip()
            mensaje = mensaje.strip()

            if nivel not in logs:
                logs[nivel] = []

            logs[nivel].append(mensaje)

    return logs
