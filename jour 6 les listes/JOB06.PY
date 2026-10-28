""" 
def L () :
    liste = [7,23,45,12,89]
    print(liste)
    print (liste[1])
    liste[3]=liste[2]+liste[4]

    print(liste)
    print(liste[-1])

 L() """

def L():
    L = [7,23,45,12,89]
    print(L)
    l1= L[0]
    L[0] = L[-1]
    L[-1] = l1
    print (L)

L()
