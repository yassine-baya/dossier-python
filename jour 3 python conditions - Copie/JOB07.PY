chaine = "abcdefghijklmnopqrstuvwxyz" * 10

longueur = 1
position = 0

while position + longueur <= len(chaine):
    print(chaine[position:position + longueur])
    position += longueur
    longueur += 1