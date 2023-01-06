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

def construireCellule(n = 0, visible = False) -> dict:
    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({visible}) n’est pas un booléen")
    if isContenuCorrect(n) == False:
        raise ValueError(f"construireCellule : le contenu {n} n’est pas correct")
    dico = {const.CONTENU:n, const.VISIBLE:visible}
    return dico

def getContenuCellule(dico:dict) -> int:
    if type_cellule(dico) == False:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return dico[const.CONTENU]

def isVisibleCellule(dico:dict) -> bool:
    if type_cellule(dico) == False:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return bool(dico[const.VISIBLE])

def setContenuCellule(dico:dict,contenu:int) -> None:
    if type_cellule(dico) == False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if contenu>8 or contenu<-1:
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n’est pas correcte.")
    dico[const.CONTENU] = contenu
    return None

def setVisibleCellule(dico:dict,visibilite:bool) -> None:
    if type_cellule(dico) == False:
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visibilite) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen")
    dico[const.VISIBLE] = visibilite
    return None

def contientMineCellule(dico:dict) -> bool:
    if type_cellule(dico) == False:
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    rep = False
    if dico[const.CONTENU] == const.ID_MINE:
        rep = True
    return rep



