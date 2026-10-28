for nombre in range(2, 1001):
    premier = True

    for diviseur in range(2, nombre):
        if nombre % diviseur == 0:
            premier = False
            break

    if premier:
        print(nombre)