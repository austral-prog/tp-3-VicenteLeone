def slice_simple():
    texto = "Awesome"
    texto = texto.lower()

    print(texto[0:3])

    middle = len(texto) // 2
    print(texto[middle - 1 : middle + 2])

    print(texto[0:4] + texto[-3:])


slice_simple()
