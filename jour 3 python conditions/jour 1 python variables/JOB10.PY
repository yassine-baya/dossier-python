# Initialisation des variables
capital = 10000
taux = 5  # taux de rendement annuel en pourcentage

# Calcul du gain annuel initial
gain = capital * taux / 100
print("Gain annuel initial :", gain, "euros")

# Augmentation du capital de 5 000 euros
capital = capital + 5000

# Augmentation du taux de rendement de 2 %
taux = taux + 2

# Calcul du nouveau gain annuel
gain = capital * taux / 100
print("Nouveau capital :", capital, "euros")
print("Nouveau taux de rendement :", taux, "%")
print("Nouveau gain annuel :", gain, "euros")

# Capital et taux après la première augmentation
capital = 15000
taux = 7

# Calcul du gain annuel avant le retrait
gain = capital * taux / 100
print("Gain annuel avant retrait :", gain, "euros")

# Retrait de 10 % du capital
retrait = capital * 10 / 100
capital = capital - retrait

# Diminution du taux de rendement de 1 %
taux = taux - 1

# Calcul du nouveau gain annuel
gain = capital * taux / 100

# Affichage des résultats
print("Montant du retrait :", retrait, "euros")
print("Montant final de l'investissement :", capital, "euros")
print("Nouveau taux de rendement :", taux, "%")
print("Nouveau gain annuel :", gain, "euros")