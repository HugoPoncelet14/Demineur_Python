# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)

def isContenuCorrect(n : int) -> bool:
    rep = False
    if type(n) == int:
        if n >= 0 and n <= 8 or n == const.ID_MINE :
            rep = True
    return rep

def construireCellule(n = 0, booleen = False) -> dict:
    if type(booleen) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({booleen}) n’est pas un booléen")
    if n>8 or n<-1:
        raise ValueError(f"construireCellule : le contenu {n} n’est pas correct")
    dico = { const.CONTENU : n , const.VISIBLE  : booleen }
    return dico








