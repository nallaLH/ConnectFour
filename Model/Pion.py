# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(color : int) -> dict:
    """
    Fonction permettant de construire un pion
    :param color: Couleur du pion à construire
    :return: Dictionnaire représentant un pion
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si l’entier ne représente pas une couleur
    """
    if type(color) != int:
        raise TypeError("construirePion : Le paramètre n’est pas de type entier")
    if color not in const.COULEURS:
        raise ValueError(f"construirePion : la couleur {color} n’est pas correcte")

    return {const.COULEUR: color, const.ID: None}

def getCouleurPion(pion: dict) -> int:
    """
    Fonction permettant de récupérer la couleur d'un pion
    :param pion: Pion dont on veut récupérer la couleur
    :return: Entier représentant la couleur du pion
    :raise TypeError: Si le paramètre n’est pas un pion (dictionnaire)
    """
    if type_pion(pion) == False:
        raise TypeError("getCouleurPion : Le paramètre n'est pas un pion")

    return pion[const.COULEUR]

def setCouleurPion(pion: dict, color: int) -> None:
    """
    Fonction permettant de modifier la couleur d'un pion
    :param pion: Pion dont on veut modifier la couleur
    :param color: Nouvelle couleur qui va être attribuée au pion
    :return: Ne retourne rien
    :raise TypeError: Si le premier paramètre n’est pas un pion
    :raise TypeError: Si le second paramètre n'est pas un entier
    :raise ValueError: Si la valeur du second paramètre ne correspond pas à une couleur
    """
    if type_pion(pion) == False:
        raise TypeError("setCouleurPion : Le premier paramètre n’est pas un pion")
    if type(color) != int:
        raise TypeError("setCouleurPion : Le second paramètre n’est pas un entier")
    if color not in const.COULEURS:
        raise ValueError(f"setCouleurPion : Le second paramètre {color} n’est pas une couleur")
    pion[const.COULEUR] = color

    return None

def getIdPion(pion: dict) -> int:
    """
    Fonction permettant de récupérer l'id d'un pion
    :param pion: Pion dont on veut récupérer l'id
    :return: Retourne l'id du pion passé en paramètre
    :raise TypeError: Si le paramètre n’est pas un pion
    """
    if type_pion(pion) == False:
        raise TypeError("getIdPion : Le paramètre n’est pas un pion")

    return pion[const.ID]

def setIdPion(pion: dict, valeur: int) -> None:
    """
    Fonction permettant de modifier l'id d'un pion
    :param pion: Pion dont on veut modifier l'id
    :param valeur: Valeur qui va modifier l'id
    :return: Ne retourne rien
    :raise TypeError: Si le premier paramètre n’est pas un pion
    :raise TypeError: Si le second paramètre n’est pas un entier
    """
    if type_pion(pion) == False:
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion ")
    if type(valeur) != int:
        raise TypeError("setIdPion : Le second paramètre n'est pas un entier")
    pion[const.ID] = valeur

    return None

