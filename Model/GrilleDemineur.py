# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(li:int, co:int) -> list:
    if type(li) != int or type(co) != int:
        raise TypeError(f" Le nombre de lignes ({type(li)}) ou de colonnes ({type(co)}) n’est pas un entier.")
    if co <= 0 or li <= 0:
        raise ValueError(f" construireGrilleDemineur : Le nombre de ligns ({li}) ou de colonnes ({co}) est négatif ou nul. ")
    grille = []
    for i in range(li):
        ligne = []
        for l in range(co):
            ligne.append(construireCellule())
        grille.append(ligne)
    return grille

def getNbLignesGrilleDemineur(g:list) -> int:
    if type_grille_demineur(g) == False:
        raise TypeError(" getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(g)

def getNbColonnesGrilleDemineur(g:list) -> int:
    if type_grille_demineur(g) == False:
        raise TypeError(" getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(g[0])

def isCoordonneeCorrecte(g:list,coord:tuple) -> bool:
    if type_grille_demineur(g) == False or type(coord) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    rep = True
    if coord[0] >= getNbLignesGrilleDemineur(g) or coord[1] >= getNbColonnesGrilleDemineur(g):
        rep = False
    return rep

def getCelluleGrilleDemineur(g:list,coord:tuple):
    if type_grille_demineur(g) == False or type(coord) != tuple:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(g,coord) == False :
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    return g[coord[0]][coord[1]]





















