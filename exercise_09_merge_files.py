def merge_files(file1, file2, output):

    with open(file1, "r") as a:
        contenido1 = a.read()

    with open(file2, "r") as b:
        contenido2 = b.read()

    with open(output, "w") as out:
        out.write(contenido1 + contenido2)
