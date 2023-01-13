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
    ''' Determine si le contenu n passé en parametre est correct ou non
        Retourne True si le contenu est correct, False sinon'''

    rep = False
    if type(n) == int:
        if n >= 0 and n <= 8 or n == const.ID_MINE :
            rep = True
    return rep

def construireCellule(n : int = 0, visible : bool = False) -> dict:
    '''Retourne un dictionnaire corespondant à une cellule sous la forme (cell = {const.CONTENU:n, const.VISIBLE:visible, const.ANNOTATION:None})'''
    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre ({visible}) n’est pas un booléen")
    if isContenuCorrect(n) == False:
        raise ValueError(f"construireCellule : le contenu {n} n’est pas correct")
    cell = {const.CONTENU : n, const.VISIBLE : visible, const.ANNOTATION : None, const.RESOLU : False}
    return cell

def getContenuCellule(cell:dict) -> int:
    '''retourne le contenu de la cellule 'cell' passée en paramètre'''
    if type_cellule(cell) == False:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")
    return cell[const.CONTENU]

def isVisibleCellule(cell:dict) -> bool:
    '''Retourne la visibilité de la cellule 'cell' passée en paramètre'''
    if type_cellule(cell) == False:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")
    return cell[const.VISIBLE]

def setContenuCellule(cell:dict,contenu:int) -> None:
    '''Modifie le contenu de la cellule 'cell' passée en paramètre par 'contenu' passé en parametre, ne retourne rien'''
    if type_cellule(cell) == False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if contenu>8 or contenu<-1:
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n’est pas correcte.")
    cell[const.CONTENU] = contenu
    return None

def setVisibleCellule(cell:dict,visibilite:bool) -> None:
    '''Modifie la visibilité de la cellule 'cell' passée en paramètre par 'visibilite' passé en parametre, ne retourne rien'''
    if type_cellule(cell) == False:
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visibilite) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen")
    cell[const.VISIBLE] = visibilite
    return None

def contientMineCellule(cell:dict) -> bool:
    '''retourne True si la cellule 'cell' passée en paramètre contient une mine et retourne False sinon'''
    if type_cellule(cell) == False:
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    rep = False
    if cell[const.CONTENU] == const.ID_MINE:
        rep = True
    return rep

def isAnnotationCorrecte(ann:str) -> bool:
    '''Retourne True si l'annotation 'ann' passée en paramètre est correcte, False sinon'''
    rep = False
    if ann == None or ann ==  const.DOUTE or ann ==  const.FLAG:
        rep = True
    return rep

def getAnnotationCellule(cell:dict) -> str:
    '''retourne l'annotation de la cellule 'cell' passée en parametre'''

    if type_cellule(cell) == False:
        raise TypeError(f"getAnnotationCellule : le paramètre valeur_du paramètre n’est pas une cellule")
    return cell.get(const.ANNOTATION,None)

def changeAnnotationCellule(cell:dict) -> None:

    '''Modifie la visibilité de la cellule 'cell' passée en paramètre par l'annotation qui sui dans le cycle de changement des annotations, ne retourne rien'''

    if type_cellule(cell) == False:
        raise TypeError(f"changeAnnotationCellule : le paramètre n’est pas une cellule")
    if cell[const.ANNOTATION] == None:
        cell[const.ANNOTATION] = const.FLAG
    elif cell[const.ANNOTATION] == const.FLAG:
        cell[const.ANNOTATION] = const.DOUTE
    elif cell[const.ANNOTATION] == const.DOUTE:
        cell[const.ANNOTATION] = None

def reinitialiserCellule(cell:dict) -> None:

    '''reinitialise la cellule 'cell' passée en paramètre en initialisant le contenu à 0, la visibilité a False et l'annotation à  None'''

    cell[const.CONTENU] = 0
    cell[const.VISIBLE] = False
    cell[const.ANNOTATION] = None
    cell[const.RESOLU] = False









