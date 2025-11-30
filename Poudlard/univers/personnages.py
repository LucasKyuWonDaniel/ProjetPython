def initialiser_personnage(nom, prenom, attributs):
    personnage = {
        "nom": nom,
        "prenom": prenom,
        "Argent" : 100,
        "Inventaire" : [],
        "Sortilèges" : [],
        "Attributs" : attributs,
    }
    return personnage

def afficher_personnage(joueur):
