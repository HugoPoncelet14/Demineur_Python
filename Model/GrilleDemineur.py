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

    ''' retourne une grille de demineur de li lignes et co colonnes'''

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
    '''Retourne le nombre de lignes de le grille 'g' passée en parametre'''

    if type_grille_demineur(g) == False:
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(g)

def getNbColonnesGrilleDemineur(g:list) -> int:
    '''Retourne le nombre de colonnes de le grille 'g' passée en parametre'''

    if type_grille_demineur(g) == False:
        raise TypeError(" getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(g[0])

def isCoordonneeCorrecte(g:list,coord:tuple) -> bool:
    '''Retourne True si la coordonnée 'coord' passée en paramètre se trouve bien dans la grille 'g' passée en paramètre, False sinon'''

    if type_grille_demineur(g) == False or type(coord) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    rep = True
    if coord[0] >= getNbLignesGrilleDemineur(g) or coord[1] >= getNbColonnesGrilleDemineur(g):
        rep = False
    return rep

def getCelluleGrilleDemineur(g:list,coord:tuple) -> dict:
    '''Retourne la cellule se situant aux coordonnées 'coord' passées en paramètres dans la grille 'g' passée en parametre '''
    if type_grille_demineur(g) == False or type(coord) != tuple:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(g,coord) == False :
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    return g[coord[0]][coord[1]]


def getContenuGrilleDemineur(g:list,coord:tuple) -> int:
    '''Retourne le contenu de la cellule se situant aux coordonnées 'coord' passées en paramètres dans la grille 'g' passée en parametre '''

    return getCelluleGrilleDemineur(g,coord)[const.CONTENU]

def setContenuGrilleDemineur(g:list,coord:tuple,n:int) -> None:
    '''Modifie le contenu de la cellule se situant aux coordonnées 'coord' passées en paramètres dans la grille 'g' passée en parametre par 'n' passé en paramètre'''

    if type(n) != int:
        raise TypeError(f"setContenuGrilleDemineur : le contenu {n} n'est pas correct")
    if (n < 0 or n > 8) and n != const.ID_MINE :
        raise ValueError(f"setContenuGrilleDemineur : La valeur du contenu {n} n'est pas correct")
    getCelluleGrilleDemineur(g,coord)[const.CONTENU] = n
    return None

def isVisibleGrilleDemineur(g:list,coord:tuple) -> int:
    '''Retourne la visibilité de la cellule se situant aux coordonnées 'coord' passées en paramètres dans la grille 'g' passée en parametre '''

    return getCelluleGrilleDemineur(g,coord)[const.VISIBLE]

def setVisibleGrilleDemineur(g:list,coord:tuple,visible:bool) -> None:
    '''Modifie la visibilité de la cellule se situant aux coordonnées 'coord' passées en paramètres dans la grille 'g' passée en parametre par 'visible' passé en paramètre'''

    if type(visible) != bool:
        raise TypeError(f"setVisibleGrilleDemineur : le type de visible {type(visible)} n'est pas correct")
    getCelluleGrilleDemineur(g, coord)[const.VISIBLE] = visible

def contientMineGrilleDemineur(g:list,coord:tuple) -> bool:
    '''Retourne True si la cellule se situant aux coordonnées 'coord' passées en paramètres dans la grille 'g' passée en parametre contient une mine, False sinon'''

    rep = False
    if getCelluleGrilleDemineur(g, coord)[const.CONTENU] == const.ID_MINE:
        rep = True
    return rep


def getCoordonneeVoisinsGrilleDemineur(g:list,coord:tuple) -> list:
    ''' Retourne une liste contenant les coordonnées des cellules voisines de la cellule se situant aux coordonnées 'coord' passées en paramètres dans la grille 'g' passée en parametre'''

    if type_grille_demineur(g) == False or type(coord) != tuple:
        raise TypeError(f"getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(g,coord) == False:
        raise IndexError(f"getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    liste_coord = []
    for i in range(3):
        for l in range(3):
            nl = coord[0]-1+i
            nc = coord[1]-1+l
            if nl >= 0 and nl < getNbLignesGrilleDemineur(g) :
                if nc >= 0 and nc < getNbColonnesGrilleDemineur(g):
                    if((nl,nc)) != coord:
                        liste_coord.append((nl,nc))
    return liste_coord

def placerMinesGrilleDemineur(g:list,nb:int,coord:tuple) -> None:
    ''' Place de façon aléatoire sauf dans la cellule se situant aux coordonnées 'coord' passées en paramètre nb passé en paramètre mines dans la grille 'g' passée en paramètre'''

    if nb < 0 or nb >= getNbLignesGrilleDemineur(g) * getNbColonnesGrilleDemineur(g):
        raise ValueError(f"placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    if isCoordonneeCorrecte(g,coord) == False:
        raise IndexError(f"placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    mines_poses = nb
    while mines_poses > 0:
        coord_mine = (randint(0,getNbLignesGrilleDemineur(g)-1),randint(0,getNbColonnesGrilleDemineur(g)-1))
        if getContenuGrilleDemineur(g,coord_mine) != const.ID_MINE and coord_mine != coord:
            setContenuGrilleDemineur(g,coord_mine,const.ID_MINE)
            mines_poses -= 1
    compterMinesVoisinesGrilleDemineur(g)
    return None

def compterMinesVoisinesGrilleDemineur(g:list) -> None:
    '''modifie le contenu de chaque cellule de la grille par le nombre de mines voisines'''

    for i in range(getNbLignesGrilleDemineur(g)):
        for l in range(getNbColonnesGrilleDemineur(g)):
            if getContenuGrilleDemineur(g,(i,l)) != const.ID_MINE:
                liste_voisines = getCoordonneeVoisinsGrilleDemineur(g,(i,l))
                nb_mines = 0
                for j in range(len(liste_voisines)):
                    if getContenuGrilleDemineur(g,liste_voisines[j]) == const.ID_MINE:
                        nb_mines += 1
                setContenuGrilleDemineur(g,(i,l),nb_mines)
    return None

def getNbMinesGrilleDemineur(g:list) -> int:
    '''retourne le nombre de mines contenues dans la grille 'g' passée en paramètre'''

    if type_grille_demineur(g) == False:
        raise ValueError(f"getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    nb_mines = 0
    for i in range(getNbLignesGrilleDemineur(g)):
        for l in range(getNbColonnesGrilleDemineur(g)):
            if contientMineGrilleDemineur(g,(i,l)):
                nb_mines += 1
    return nb_mines

def getAnnotationGrilleDemineur(g:list,coord:tuple):
    '''retourne l'annotation de la cellule se situant aux coordonnées 'coord' passées en paramètres dans la grille 'g' passée en parametre'''

    return getCelluleGrilleDemineur(g, coord)[const.ANNOTATION]

def getMinesRestantesGrilleDemineur(g:list):
    '''Retourne le nombre de Mines non visibles et dont l'annotation n'est pas un drapeau restantes dans la grille 'g' passée en paramètre'''

    nb_mines_marques = 0
    for i in range(getNbLignesGrilleDemineur(g)):
        for l in range(getNbColonnesGrilleDemineur(g)):
            if getCelluleGrilleDemineur(g,(i,l))[const.ANNOTATION] == const.FLAG:
                nb_mines_marques += 1
    return getNbMinesGrilleDemineur(g) - nb_mines_marques

def gagneGrilleDemineur(g:list) -> bool:
    '''retourne True si la partie de démineur est gagnée pour la grille 'g' passée en paramètre, False sinon'''

    rep = True
    visibles = 0
    for i in range(getNbLignesGrilleDemineur(g)):
        for l in range(getNbColonnesGrilleDemineur(g)):
            if contientMineGrilleDemineur(g,(i,l)) == False :
                if isVisibleGrilleDemineur(g,(i,l)):
                    visibles += 1
            else :
                if isVisibleGrilleDemineur(g,(i,l)):
                    rep = False
                if getAnnotationGrilleDemineur(g,(i,l)) != const.FLAG:
                    rep = False
    if visibles + getNbMinesGrilleDemineur(g) != getNbLignesGrilleDemineur(g)*getNbColonnesGrilleDemineur(g):
        rep = False
    return rep

def perduGrilleDemineur(g:list) -> bool:
    '''retourne True si la partie de démineur est perdue pour la grille 'g' passée en paramètre, False sinon'''

    rep = False
    for i in range(getNbLignesGrilleDemineur(g)):
        for l in range(getNbColonnesGrilleDemineur(g)):
            if contientMineGrilleDemineur(g,(i,l)) and isVisibleGrilleDemineur(g,(i,l)):
                rep = True
    return rep

def reinitialiserGrilleDemineur(g:list) -> None:
    '''Reinitialise la grille 'g' passée en paramètre (réinitialise toutes ses cellules)'''

    for i in range(getNbLignesGrilleDemineur(g)):
        for l in range(getNbColonnesGrilleDemineur(g)):
            reinitialiserCellule(getCelluleGrilleDemineur(g,(i,l)))
    return None

def decouvrirGrilleDemineur(g:list,coord:tuple) -> set:
    '''Cette fonction rend visible la cellule correspondant à la coordonnée 'coord' passée en paramètre dans la grille 'g' passée en paramètre.
       Si cette cellule contient 0 mine dans le voisinage, la fonction découvre les cellules dans le voisinage.
       Si une des cellules du voisinage contient 0 mine, on relance le processus.
       La fonction retourne l’ensemble des coordonnées des cellules rendues visibles.'''

    lst_coord = [coord]
    ajout = True
    while ajout == True:
        ajout = False
        for i in range(len(lst_coord)):
            if getContenuGrilleDemineur(g,lst_coord[i]) == 0:
                for l in range(len(getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i]))):
                    if not getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i])[l] in lst_coord:
                        lst_coord.append((getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i]))[l])
                        setVisibleGrilleDemineur(g,(getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i])[l]),True)
                        ajout = True
    return lst_coord



def simplifierGrilleDemineur(g:list,coord:tuple) -> set:
    '''Cette fonction vérifie déjà que la cellule correspondant à la coordonnée 'coord' passée en paramètre dans la grille 'g' passée en paramètre cliquée est bien visible.
    Si ce n’est pas le cas, elle retourne un ensemble vide.
    Dans le cas où la case est visible, la fonction compte le nombre de drapeaux dans le voisinage de cette case.
    Si ce nombre correspond exactement au contenu de la case, la fonction rend toutes les autres cases voisines visibles.
    On relance alors le procédé sur les cases rendues visibles.
    La fonction retourne l’ensemble des coordonnées des cases rendues visibles.'''

    if isVisibleGrilleDemineur(g,coord) == True:
        lst_coord = [coord]
        simp = True
        while simp == True:
            simp = False
            for i in range(len(lst_coord)):
                if getContenuGrilleDemineur(g, lst_coord[i]) > 0 :
                    nb_drap = 0
                    for j in range(len(getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i]))):
                        if getAnnotationGrilleDemineur(g,getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i])[j]) == const.FLAG:
                            nb_drap += 1
                    if getContenuGrilleDemineur(g,lst_coord[i]) == nb_drap:
                        for l in range(len(getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i]))):
                            if getAnnotationGrilleDemineur(g,getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i])[l]) != const.FLAG:
                                if not getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i])[l] in lst_coord :
                                    if getCoordonneeVoisinsGrilleDemineur(g,lst_coord[i])[l] != const.ID_MINE:
                                        lst_coord.append((getCoordonneeVoisinsGrilleDemineur(g, lst_coord[i]))[l])
                                        setVisibleGrilleDemineur(g, (getCoordonneeVoisinsGrilleDemineur(g, lst_coord[i])[l]),True)
                                        simp = True
    else :
        lst_coord = []
    return lst_coord


def ajouterFlagsGrilleDemineur(g:list,coord:tuple) -> set :
    nb_non_decouv = 0
    liste_drap = []
    for i in range(len(getCoordonneeVoisinsGrilleDemineur(g,coord))):
        if isVisibleGrilleDemineur(g,(getCoordonneeVoisinsGrilleDemineur(g,coord)[i])) == False:
            nb_non_decouv += 1
    if nb_non_decouv == getContenuGrilleDemineur(g,coord):
        for j in range(len(getCoordonneeVoisinsGrilleDemineur(g,coord))):
            if isVisibleGrilleDemineur(g,(getCoordonneeVoisinsGrilleDemineur(g,coord)[j])) == False:
                getCelluleGrilleDemineur(g,(getCoordonneeVoisinsGrilleDemineur(g,coord)[j]))[const.ANNOTATION] = const.FLAG
                liste_drap.append(getCoordonneeVoisinsGrilleDemineur(g,coord)[j])
    return liste_drap

def simplifierToutGrilleDemineur(g:list) -> tuple:
    liste_visible = []
    liste_drapeau = []
    modif = True
    while modif == True:
        modif = False
        for i in range(getNbLignesGrilleDemineur(g)):
            for l in range(getNbColonnesGrilleDemineur(g)):
                for j in range(len(simplifierGrilleDemineur(g,(i,l)))):
                    if not simplifierGrilleDemineur(g,(i,l))[j] in liste_visible:
                        liste_visible.append(simplifierGrilleDemineur(g,(i,l))[j])
                        modif = True
                for u in range(len(ajouterFlagsGrilleDemineur(g,(i,l)))):
                    if not ajouterFlagsGrilleDemineur(g,(i,l))[u] in liste_drapeau:
                        liste_drapeau.append(ajouterFlagsGrilleDemineur(g,(i,l))[u])
                        modif = True
                simplifierGrilleDemineur(g, (i, l))
                ajouterFlagsGrilleDemineur(g, (i, l))
    return (liste_visible,liste_drapeau)




























































