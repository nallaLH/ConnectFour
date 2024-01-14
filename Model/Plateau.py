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

    while (plateau[ligne_i][column] is not None) and (ligne_i > 0):
        ligne_i -= 1
    if plateau[ligne_i][column] is None:
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
    i = 0
    while i < const.NB_LINES:
        j = 0
        while j <= (const.NB_COLUMNS - 4):
            if (plateau[i][j] is not None and getCouleurPion(plateau[i][j]) == couleur) and (plateau[i][j + 1] is not None and getCouleurPion(plateau[i][j + 1]) == couleur) and (plateau[i][j + 2] is not None and getCouleurPion(plateau[i][j + 2]) == couleur) and (plateau[i][j + 3] is not None and getCouleurPion(plateau[i][j + 3]) == couleur):
                if j != 0:
                    if plateau[i][j-1] is not None and getCouleurPion(plateau[i][j-1]) != couleur:
                        res += [plateau[i][j], plateau[i][j + 1], plateau[i][j + 2], plateau[i][j + 3]]
                        # res += [i,j,i,j + 1, i,j + 2,i,j + 3]
                else:
                    res += [plateau[i][j], plateau[i][j + 1], plateau[i][j + 2], plateau[i][j + 3]]
                    # res += [i,j,i,j + 1, i,j + 2,i,j + 3]
            j += 1
        i += 1
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
    i = const.NB_LINES-1
    while i >= 3:
        j = 0
        while j < const.NB_COLUMNS:
            if (plateau[i][j] is not None and getCouleurPion(plateau[i][j]) == couleur) and (plateau[i-1][j] is not None and getCouleurPion(plateau[i-1][j]) == couleur) and (plateau[i-2][j] is not None and getCouleurPion(plateau[i-2][j]) == couleur) and (plateau[i-3][j] is not None and getCouleurPion(plateau[i-3][j]) == couleur):
                if i != (const.NB_LINES-1) :
                    if plateau[i+1][j] is not None and getCouleurPion(plateau[i+1][j]) != couleur:
                        res += [plateau[i][j], plateau[i-1][j], plateau[i-2][j], plateau[i-3][j]]
                        # res += [i,j,i-1,j, i-2,j,i-3,j]
                else:
                    res += [plateau[i][j], plateau[i-1][j], plateau[i-2][j], plateau[i-3][j]]
                    # res += [i,j,i-1,j, i-2,j,i-3,j]
            j += 1
        i -= 1
    return res

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction permettant de détecter si 4 pions se suivent en diagonale directe sur le plateau
    :param plateau: Plateau sur lequel nous allons détecter les pions
    :param couleur: Couleur des pions que nous allons regarder
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
    i = const.NB_LINES-1
    while i >= 3:
        j = const.NB_COLUMNS-1
        while j >= 3:

            if (plateau[i][j] is not None and getCouleurPion(plateau[i][j]) == couleur) and (
                    plateau[i - 1][j - 1] is not None and getCouleurPion(plateau[i - 1][j - 1]) == couleur) and (
                    plateau[i - 2][j - 2] is not None and getCouleurPion(plateau[i - 2][j - 2]) == couleur) and (
                    plateau[i - 3][j - 3] is not None and getCouleurPion(plateau[i - 3][j - 3]) == couleur):

                if i != (const.NB_LINES-1) and j != (const.NB_COLUMNS-1):

                    if plateau[i + 1][j + 1] is not None and getCouleurPion(plateau[i + 1][j + 1]) != couleur:
                        res += [plateau[i][j], plateau[i - 1][j - 1], plateau[i - 2][j - 2], plateau[i - 3][j - 3]]
                        # res += i, j, " ",i + 1, j + 1, " ",i + 2, j + 2, " ",i + 3, j + 3, " "

                else:
                    res += [plateau[i][j], plateau[i - 1][j - 1], plateau[i - 2][j - 2], plateau[i - 3][j - 3]]
                    # res += i, j, " ", i + 1, j + 1, " ", i + 2, j + 2, " ", i + 3, j + 3, " "
            j -= 1
        i -= 1

    return res

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction permettant de détecter si 4 pions se suivent en diagonale indirecte sur le plateau
    :param plateau: Plateau sur lequel nous allons détecter les pions
    :param couleur: Couleur des pions que nous allons regarder
    :return: Retourne une liste de pions de la couleur donnée en paramètre qui sont alignés par 4, sinon retourne une liste vide
    :raise TypeError: Si le premier paramètre n'est pas un plateau
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si la valeur du second paramètre ne correspond pas à une couleur
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectelPlateau : Le second paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"detecter4diagonaleIndirectePlateau : Le second paramètre {couleur} n’est pas une couleur")

    res = []
    i = const.NB_LINES - 1
    while i >= (const.NB_LINES - 4):
        j = 0
        while j <= (const.NB_COLUMNS - 4):

            if (plateau[i][j] is not None and getCouleurPion(plateau[i][j]) == couleur) and (plateau[i - 1][j + 1] is not None and getCouleurPion(plateau[i - 1][j + 1]) == couleur) and (plateau[i - 2][j + 2] is not None and getCouleurPion(plateau[i - 2][j + 2]) == couleur) and (plateau[i - 3][j + 3] is not None and getCouleurPion(plateau[i - 3][j + 3]) == couleur):

                if i != (const.NB_LINES-1) and j != 0:

                    if plateau[i + 1][j - 1] is not None and getCouleurPion(plateau[i + 1][j - 1]) != couleur:
                        if (i - 3) >= 0 and (j + 3) <= 6:
                            res += [plateau[i][j], plateau[i - 1][j + 1], plateau[i - 2][j + 2], plateau[i - 3][j + 3]]
                            # res += i, j, " ",i - 1, j + 1, " ",i - 2, j + 2, " ",i - 3, j + 3, " "

                else:
                    if (i-3) >= 0 and (j+3) <= 6:
                        res += [plateau[i][j], plateau[i - 1][j + 1], plateau[i - 2][j + 2], plateau[i - 3][j + 3]]
                        # res += i,j," ",i-1,j+1," ",i-2,j+2," ",i-3,j+3, " "
            j += 1
        i -= 1

    return res


def getPionsGagnantsPlateau(plateau: list) -> list:
    """
    Fonction donnant toutes les séries de 4 pions allignés trouvées pour les deux couleurs, s'il n'y en a pas, renvoie une liste vide
    :param plateau: Plateau sur lequel nous allons récupérer les séries gagnantes
    :return: Retourne la liste de toutes les séries de 4 pions allignés
    :raise TypeError: Si le paramètre n'est pas un plateau
    """
    if type_plateau(plateau) == False:
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n’est pas un plateau")
    res = []
    res += detecter4horizontalPlateau(plateau, const.JAUNE) + detecter4verticalPlateau(plateau, const.JAUNE) + detecter4diagonaleDirectePlateau(plateau, const.JAUNE) + detecter4diagonaleIndirectePlateau(plateau, const.JAUNE) + detecter4horizontalPlateau(plateau, const.ROUGE) + detecter4verticalPlateau(plateau, const.ROUGE) + detecter4diagonaleDirectePlateau(plateau, const.ROUGE) + detecter4diagonaleIndirectePlateau(plateau, const.ROUGE)

    return res


def isRempliPlateau(plateau: list) -> bool:
    """
    Fonction permettant de savoir si un plateau est rempli ou non
    :param plateau: Plateau sur lequel la partie se déroule
    :return: Retourne un booléen True si le plateau est rempli, False dans le cas contraire
    :raise TypeError: Si le paramètre n'est pas un plateau
    """
    if type_plateau(plateau) == False:
        raise TypeError("isRempliPlateau : Le paramètre n'est pas un plateau")
    res = False
    i = j = 0
    if plateau[i][j] is not None and plateau[i][j+1] is not None and plateau[i][j+2] is not None and plateau[i][j+3] is not None and plateau[i][j+4] is not None and plateau[i][j+5] is not None and plateau[i][j+6] is not None:
        res = True
    return res

# def placerPionLignePlateau(plateau: list, pion: dict, ligne: int, left: bool) -> tuple:
#     """
#     Fonction plaçant un pion sur la ligne indiquée soit par la gauche, soit par la droite
#     :param plateau: Plateau dans lequel le pion va être inséré
#     :param pion: Pion qui va être inséré
#     :param ligne: Numéro de ligne dans laquelle le pion va être inséré
#     :param left: Vaut True si le pion est inséré à gauche, False si inséré à droite
#     :return: Retourne un tuple constitué de la liste des pions poussés et un entier correspond au numéro de ligne où se retrouve le dernier pion de la liste (None s'il ne change pas de ligne)
#     :raise TypeError: Si le premier paramètre n'est pas un plateau
#     :raise TypeError: Si le deuxième paramètre n'est pas un pion
#     :raise TypeError: Si le troisième paramètre n'est pas un entier
#     :raise ValueError: Si le troisième paramètre ne correspond pas à une ligne
#     :raise TypeError: Si le quatrième paramètre n'est pas un booléen
#     """
#     if type_plateau(plateau) == False:
#         raise TypeError("placerPionLignePlateau : Le premier paramètre n’est pas un plateau")
#     if type_pion(pion) == False:
#         raise TypeError("placerPionLignePlateau : Le second paramètre n’est pas un pion")
#     if type(ligne) != int:
#         raise TypeError("placerPionLignePlateau : le troisième paramètre n’est pas un entier")
#     if ligne < 0 and ligne > (const.NB_LINES-1):
#         raise ValueError(f"placerPionLignePlateau : Le troisième paramètre {ligne} ne désigne pas une ligne")
#     if type(left) != bool:
#         raise TypeError("placerPionLignePlateau : le quatrième paramètre n’est pas un booléen")
#
#     L = []
#     if left == True:
#         if plateau[ligne][0] is None:
#             plateau[ligne][0] = pion
#
#
#
#
#
#     if left == False:
#         if plateau[ligne][const.NB_COLUMNS-1] is None:
#             plateau[ligne][const.NB_COLUMNS-1] = pion
#
#     return None



def encoderPlateau(plateau: list) -> str:
    """
    Fonction permettant d'encoder un plateau
    :param plateau: Plateau qui va être encodé
    :return: Retourne une chaîne de caractères correspondant au plateau encodé
    :raise TypeError: Si le paramètre n'est pas un plateau
    """
    if type_plateau(plateau) == False:
        raise TypeError("encoderPlateau : Le paramètre n'est pas un plateau")

    res = ''
    for i in range(0, const.NB_LINES):

        for j in range(0, const.NB_COLUMNS):

            if plateau[i][j] is None:
                res += "_"
            elif plateau[i][j] is not None and getCouleurPion(plateau[i][j]) == const.ROUGE:
                res += "R"
            else:
                res += "J"

    return res
