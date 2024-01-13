from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau() -> list:
    """
    Fonction permettant de construire un plateau de const.NB_LINES lignes et const.NB_COLUMNS colonnes
    :return: Retourne un tableau 2D vide
    """
    tableau = []
    for i in range(const.NB_LINES):
        ligne = []
        for j in range(const.NB_COLUMNS):
            ligne.append(None)
        tableau.append(ligne)
    return tableau

def placerPionPlateau(plateau: list, pion: dict, column: int) -> int:
    """
    Fonction permettant de déposer un pion dans la colonne indiquée
    :param plateau: Plateau dans lequel le pion va être déposé
    :param pion: Pion qui va être déposé
    :param column: Colonne dans laquelle le pion va être joué
    :return: Retourne le numéro de ligne où se trouve le pion, si la colonne est déjà pleine, retourne -1
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le deuxième paramètre n'est pas un pion
    :raise TypeError: Si le troisième paramètre n'est pas un entier
    :raise ValueError: Si la valeur de la colonne n'est pas correcte
    """
    if type_plateau(plateau) == False:
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type_pion(pion) == False:
        raise TypeError("placerPionPlateau : Le deuxième paramètre n'est pas un pion")
    if type(column) != int:
        raise TypeError("placerPionPlateau : Le troisième paramètre n'est pas un entier")
    if (column >= const.NB_COLUMNS) or (column < 0):
        raise ValueError(f"placerPionPlateau : La valeur de la colonne {column} n'est pas correcte")

    ligne_i = const.NB_LINES - 1
    res = -1

    while (plateau[ligne_i][column] != None) and (ligne_i > 0):
        ligne_i -= 1
    if plateau[ligne_i][column] == None:
        plateau[ligne_i][column] = pion
        res = ligne_i
    return res

def toStringPlateau(plateau: list) -> str:
    """
    Fonction convertissant le plateau en chaine de caractères
    :param plateau: Plateau qui va être converti en chaine de caractères
    :return: Retourne le plateau en chaine de caractères
    """
    plat = ""
    for i in range(len(plateau)):
        plat += "|"
        for j in range(len(plateau[i])):
            if plateau[i][j] == None:
                plat += ' '
            else:
                if getCouleurPion(plateau[i][j]) == const.JAUNE:
                    plat += "\x1B[43m \x1B[0m"
                else:
                    plat += "\x1B[41m \x1B[0m"
            plat += "|"
        plat += "\n"
    plat += "---------------\n"
    plat += " 0 1 2 3 4 5 6"

    return plat


def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction permettant de détecter si 4 pions se suivent à l'horizontale sur le plateau
    :param plateau: Plateau sur lequel nous allons détecter les pions
    :param color: Couleur des pions que nous allons regarder
    :return: Retourne une liste de pions de la couleur donnée en paramètre qui sont alignés par 4, sinon retourne une liste vide
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si la valeur du second paramètre ne correspond pas à une couleur
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"detecter4horizontalPlateau : Le second paramètre {couleur} n’est pas une couleur")

    res = []
    for i in range(const.NB_LINES):
        nbPion = []
        j = 0
        while j < const.NB_COLUMNS:
            if plateau[i][j] is not None and plateau[i][j][const.COULEUR] == couleur:
                nbPion.append(plateau[i][j])
            else:
                if len(nbPion) >= 4:
                    res += nbPion[:4]
                nbPion = []
            j += 1
        if len(nbPion) >= 4:
            res += nbPion[:4]

    return res

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction permettant de détecter si 4 pions se suivent à la verticale sur le plateau
    :param plateau: Plateau sur lequel nous allons détecter les pions
    :param color: Couleur des pions que nous allons regarder
    :return: Retourne une liste de pions de la couleur donnée en paramètre qui sont alignés par 4, sinon retourne une liste vide
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si la valeur du second paramètre ne correspond pas à une couleur
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"detecter4verticalPlateau : Le second paramètre {couleur} n’est pas une couleur")

    res = []
    for i in range(const.NB_COLUMNS):
        nbPion = []
        j = 0
        while j < const.NB_LINES:
            if plateau[j][i] is not None and plateau[j][i][const.COULEUR] == couleur:
                nbPion.append(plateau[j][i])
            else:
                if len(nbPion) >= 4:
                    res += nbPion[:4]
                nbPion = []
            j += 1
        if len(nbPion) >= 4:
            res += nbPion[:4]

    return res

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction permettant de détecter si 4 pions se suivent en diagonale directe sur le plateau
    :param plateau: Plateau sur lequel nous allons détecter les pions
    :param color: Couleur des pions que nous allons regarder
    :return: Retourne une liste de pions de la couleur donnée en paramètre qui sont alignés par 4, sinon retourne une liste vide
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si la valeur du second paramètre ne correspond pas à une couleur
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectelPlateau : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"detecter4diagonaleDirectePlateau : Le second paramètre {couleur} n’est pas une couleur")

    res = []
    i = 0
    while i <= (const.NB_LINES - 4):
        j = 0
        while j <= (const.NB_COLUMNS - 4):

            if (plateau[i][j] is not None and getCouleurPion(plateau[i][j]) == couleur) and (plateau[i+1][j+1] is not None and getCouleurPion(plateau[i+1][j+1]) == couleur) and (plateau[i+2][j+2] is not None and getCouleurPion(plateau[i+2][j+2]) == couleur) and (plateau[i+3][j+3] is not None and getCouleurPion(plateau[i+3][j+3]) == couleur):

                if i != 0 and j != 0:

                    if plateau[i - 1][j - 1] is not None and getCouleurPion(plateau[i - 1][j - 1]) != couleur:
                        res += [plateau[i][j], plateau[i + 1][j + 1], plateau[i + 2][j + 2], plateau[i + 3][j + 3]]

                    else:
                        res += [plateau[i][j], plateau[i + 1][j + 1], plateau[i + 2][j + 2], plateau[i + 3][j + 3]]

            j += 1
        i += 1

    return res


