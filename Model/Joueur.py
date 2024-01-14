from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *


#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
                                           and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
                                       not type_plateau(joueur[const.PLATEAU])):
        return False
    return True


def construireJoueur(couleur: int) -> dict:
    """
    Fonction permettant de construire un joueur
    :param color: Couleur du joueur à construire
    :return: Dictionnaire représentant un joueur
    :raise TypeError: Si le paramètre n’est pas un entier
    :raise ValueError: Si l’entier ne représente pas une couleur
    """
    if type(couleur) != int:
        raise TypeError("construireJoueur : Le paramètre n’est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"construireJoueur : L'entier donné {couleur} n’est pas une couleur")

    return {const.COULEUR: couleur, const.PLATEAU: None, const.PLACER_PION: None}


def getCouleurJoueur(joueur: dict) -> int:
    """
    Fonction permettant de récupérer la couleur du joueur
    :param joueur: Joueur dont on veut récupérer la couleur
    :return: Entier représentant la couleur du joueur
    :raise TypeError: Si le paramètre n’est pas un joueur
    """
    if type_joueur(joueur) == False:
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")

    return joueur[const.COULEUR]


def getPlateauJoueur(joueur: dict) -> list:
    """
    Fonction permettant de récupérer le plateau contenu dans le dictionnaire du joueur
    :param joueur: Joueur dont on veut récupérer le plateau contenu dans son dictionnaire
    :return: Liste représentant le plateau
    :raise TypeError: Si le paramètre n’est pas un joueur
    """
    if type_joueur(joueur) == False:
        raise TypeError("getPlateauJoueur : le paramètre ne correspond pas à un joueur")

    return joueur[const.PLATEAU]


def getPlacerPionJoueur(joueur: dict) -> callable:
    """
    Fonction permettant de récupérer la fonction contenue dans le dictionnaire du joueur
    :param joueur: Joueur dont on veut récupérer la fonction contenue dans son dictionnaire
    :return: Fonction contenue dans le dictionnaire
    :raise TypeError: Si le paramètre n’est pas un joueur
    """
    if type_joueur(joueur) == False:
        raise TypeError("getPlacerPionJoueur : le paramètre ne correspond pas à un joueur")
    return joueur[const.PLACER_PION]


def getPionJoueur(joueur: dict) -> dict:
    """
    Fonction permettant de construire un pion en utilisant la couleur du joueur
    :param joueur: Joueur dont la couleur va permettre de construire un pion
    :return: Pion construit avec la couleur du joueur
    :raise TypeError: Si le paramètre ne correspond pas à un joueur
    """
    if type_joueur(joueur) == False:
        raise TypeError("getPionJoueur : le paramètre ne correspond pas à un joueur")
    return construirePion(getCouleurJoueur(joueur))


def setPlateauJoueur(joueur: dict, plateau: list) -> None:
    """
    Fonction permettant d'affecter un plateau à un joueur
    :param joueur: Joueur à qui on va affecter un plateau
    :param plateau: Plateau qui va être affecté
    :return: Ne retourne rien
    :raise TypeError: Si le premier paramètre n'est pas un joueur
    :raise TypeError: Si le second paramètre n'est pas un plateau
    """
    if not type_joueur(joueur):
        raise TypeError("setPlateauJoueur : Le premier paramètre ne correspond pas à un joueur")
    if not type_plateau(plateau):
        raise TypeError("setPlateauJoueur : Le second paramètre ne correspond pas à un plateau")
    joueur[const.PLATEAU] = plateau

    return None


def setPlacerPionJoueur(joueur: dict, fonction: callable) -> None:
    """
    Fonction permettant d'affecter une fonction à un joueur
    :param joueur: Joueur à qui on va affecter une fonction
    :param fonction: Fonction qui va être affectée
    :return: Ne retourne rien
    :raise TypeError: Si le premier paramètre n'est pas un joueur
    :raise TypeError: Si le second paramètre n'est pas un plateau
    """
    if not type_joueur(joueur):
        raise TypeError("setPlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")
    if not callable(fonction):
        raise TypeError("setPlacerPion : le second paramètre n'est pas une fonction")
    joueur[const.PLACER_PION] = fonction

    return None


