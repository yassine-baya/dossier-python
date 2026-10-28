a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

if a <= 0 or b <= 0 or c <= 0:
    print("Impossible de construire un triangle")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Impossible de construire un triangle")
else:
    print("Le triangle est possible")

    if a == b == c:
        print("Le triangle est équilatéral")
    elif a == b or a == c or b == c:
        print("Le triangle est isocèle")
    elif (a**2 + b**2 == c**2 or
          a**2 + c**2 == b**2 or
          b**2 + c**2 == a**2):
        print("Le triangle est rectangle")
    else:
        print("Le triangle est quelconque")
