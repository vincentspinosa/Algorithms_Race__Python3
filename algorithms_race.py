# -*- coding: utf-8 -*-

from random import randint
import time

#CALCUL DE LA VITESSE :

class Temps :
  def __init__(self, fonction, param_f) :
    t1 = time.time()
    fonction(param_f)
    t2 = time.time()
    self.resultat = t2 - t1
    return None

#ALGORITHME : (définition)

class Algorithme :
  def __init__(self, nom, fonction) :
    self.nom = nom
    self.fonction = fonction
    return None

algos = []

#COURSE : (définition)

class Init :
  def __init__(self) :
    try :
      inpt = int(input('\nEntrez le nombre de valeurs contenues dans l\'array (15 par défaut, min 2, max 150) : '))
    except ValueError :
      inpt = 15
    if (inpt < 2) :
      inpt = 2
    elif (inpt > 150) :
      inpt = 150
    self.array = []
    i = 0
    while (i < inpt) :
      x = randint(1, 100000)
      int(x)
      self.array.append(x)
      i += 1
    return None

class Course :
  def __init__(self) :
    a = Init()
    arrayCpy = a.array.copy()
    i = 0
    meilleur_res = None
    while (i < len(algos)) :
      print("\n% s" % (algos[i].nom))
      print("Array à trier : % s" % (a.array))
      print("Tri en cours...")
      resultat = Temps(algos[i].fonction, a.array).resultat
      print("Résultat : % s" % (a.array))
      a.array = arrayCpy.copy()
      print("Temps de % s : % s" % (algos[i].nom, resultat))
      if (meilleur_res == None or resultat < meilleur_res) :
        meilleur_res = resultat
        meilleur_algo = [algos[i].nom]
      elif (meilleur_res == resultat) :
        meilleur_algo.append(algos[i].nom)
      i += 1
    self.vainqueur = meilleur_algo
    print("\n% s gagne avec un temps de % s !" % (self.vainqueur, meilleur_res))
    Nouvelle_Course()
    return None

class Nouvelle_Course :
  def __init__(self) :
    print("\nVoulez-vous faire une nouvelle course ?")
    print("1 : Oui")
    print("2 : Non")
    try :
      ipt = int(input("\nEntrez la valeur correspondant à l'action désirée : "))
    except ValueError :
      ipt = 3
    if (ipt == 1) :
      Course()
    elif (ipt == 2) :
      print("\nAu revoir !")
    else :
      Nouvelle_Course()
    return None

#ALGORITHMES :

def tri_simple(array) :
  i = 0
  k = int(len(array))
  while (i < k) :
    j = i + 1
    while (j < k) :
      if (j < k and array[j] < array[i]) :
        array[i], array[j] = array[j], array[i]
        i = 0
        j = 1
      else :
        j += 1
    i += 1
  return array

def tri_milieu_vers_debut_fin(array) :
  a = int(len(array) / 2)
  i = a
  while (i > 0) :
    j = i - 1
    while (j >= 0) :
      if (array[j] > array[i]) :
        array[i], array[j] = array[j], array[i]
        i = a
        j = i - 1
      else :
        j -= 1
    i -= 1
  i = a
  while (i < (len(array) - 1)) :
    j = i + 1
    while (j < len(array)) :
      if (array[j] < array[i]) :
        array[i], array[j] = array[j], array[i]
        i = a
        j = i + 1
      else :
        j += 1
    i += 1
  tri_simple(array)
  return array

def tri_debut_fin_vers_milieu(array) :
  a = len(array)
  b = int(a / 2)
  i = 0
  while (i < b ) :
    j = i + 1
    while (j <= b) :
      if (array[j] < array[i]) :
        array[i], array[j] = array[j], array[i]
        i = 0
        j = i + 1
      else :
        j += 1
    i += 1
  k = int(a - 1)
  i = k
  while (i > b) :
    j = i - 1
    while (j >= b) :
      if (array[j] > array[i]) :
        array[i], array[j] = array[j], array[i]
        i = k
        j = i - 1
      else :
        j -= 1
    i -= 1
  tri_simple(array)
  return array

Algo_TS = Algorithme('Algo_Tri_Simple', tri_simple)
algos.append(Algo_TS)
Algo_M_DF = Algorithme('Algo_Tri_Milieu_Vers_Début_Fin', tri_milieu_vers_debut_fin)
algos.append(Algo_M_DF)
Algo_DF_M = Algorithme('Algo_Tri_Début_Fin_Vers_Milieu', tri_debut_fin_vers_milieu)
algos.append(Algo_DF_M)

#ACCUEIL :

class Bienvenue :
  def __init__(self) :
    print("Bienvenue dans la course des algorithmes !")
    print("Dans ce jeu, plusieurs algorithmes ont pour tâche de trier un array contenant des valeurs aléatoires.")
    print("Ce sera à vous, l'utilisateur, d'indiquer le nombre de valeurs contenues dans l'array à trier.")
    return None

#MAIN :

class Main :
  def __init__(self) :
    Bienvenue()
    Course()
    return None

#JEU :

Main()

