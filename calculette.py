# coding=utf-8

#Programme destiné à la conversion d'une note (par exemple sur 20) sur une autre base (par exemple 50)

def calcul(a, b, c):
    resultat = a / b * c
    return int(resultat)

def start():
    while True:
        print("Quelle est la note à convertir (ex.: 09/20) ?", end=" ")
        entree_note = input()
        note  = int(entree_note[0:2])
        coeff_depart  = int(entree_note[3:])
        coeff_dest = 50
        resultat = calcul(note, coeff_depart, coeff_dest)
        print("Sur quelle valeur doit-on la convertir (ex.: ", resultat, "/", coeff_dest,") ?", end=" ")
        entree_coeff_dest = input()
        coeff_dest = int(entree_coeff_dest)
        resultat = calcul(note, coeff_depart, coeff_dest)
        print("Résultat: ", resultat, "/", coeff_dest)
        print()
        start()

print("Bienvenue !")
start()
