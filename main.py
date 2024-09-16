#### Fonction secondaire
"""
author : oscar.brault@edu.esiee.fr
"""

def ispalindrome(p):
    """
    Détermine si une phrase/mot est un palindrome en retournant
    la phrase ou le mot et vérifiant si elle est identique
    """
    # votre code ici
    p1=""
    for i in p:
        if i!=" ":
            p1+=i 
    print(p1)
    x = "éêèêëàô"
    y = "eeeeeao"
    mytable = str.maketrans(x, y)
    if p1.translate(mytable)[::-1] == p1.translate(mytable):
        return True
    return False

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    '''
    Retourne les résultats de différents mots de test
    '''
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
