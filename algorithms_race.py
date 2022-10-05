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

  def __repr__(self) :
    return f"Resultat : {self.resultat}"

 
#ALGORITHME : (définition)

class Algorithme :
  def __init__(self, nom, fonction) :
    self.nom = nom
    self.fonction = fonction
    return None

  def __repr__(self) :
    return f"Algorithme : {self.nom}, Fonction : {self.fonction}"

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
    self.input = inpt
    self.array = []
    i = 0
    while (i < inpt) :
      x = randint(1, 100000)
      int(x)
      self.array.append(x)
      i += 1
    print(f"L'array contient {inpt} valeurs à trier !")
    return None

  def __repr__(self) :
    return f"Input : {self.input} \n Array : {self.array}"

class Course :
  def __init__(self) :
    a = Init()
    arrayCpy = a.array.copy()
    i = 0
    meilleur_res = None
    while (i < len(algos)) :
      print('\n')
      print(f"{algos[i].nom}")
      print(f"Array à trier : {a.array}")
      print("Tri en cours...")
      resultat = Temps(algos[i].fonction, a.array).resultat
      print(f"Résultat : {a.array}")
      a.array = arrayCpy.copy()
      print(f"Temps de {algos[i].nom} : {resultat}")
      if (meilleur_res == None or resultat < meilleur_res) :
        meilleur_res = resultat
        meilleur_algo = [algos[i].nom]
      elif (meilleur_res == resultat) :
        meilleur_algo.append(algos[i].nom)
      i += 1
    self.vainqueur = meilleur_algo
    self.meilleur_temps = meilleur_res
    print('\n')
    print(f"{self.vainqueur} gagne avec un temps de {self.meilleur_temps} !")
    Nouvelle_Course()
    return None

  def __repr__(self) :
    return f"Vainqueur : {self.vainqueur} \n Meilleur temps : {self.meilleur_temps}"

class Nouvelle_Course :
  def __init__(self) :
    print("\nVoulez-vous faire une nouvelle course ?")
    print("1 : Oui")
    print("2 : Non")
    try :
      self.ipt = int(input("\nEntrez la valeur correspondant à l'action désirée : "))
    except ValueError :
      self.ipt = 3
    if (self.ipt == 1) :
      Course()
    elif (self.ipt == 2) :
      print("\nAu revoir !")
    else :
      Nouvelle_Course()
    return None

  def __repr__(self) :
    return f"Option choisie : {self.ipt}"

 
#ALGORITHMES :

def tri(array, depart, fin) :
  index_boucle = depart
  fin_boucle = fin
  if (depart < fin) :
    while (index_boucle < fin_boucle) :
      j = index_boucle + 1
      while (j < fin_boucle) : # inférieur car on commence à array[0] hors la longueur commence à 1 si elle existe
        if (array[j] < array[index_boucle]) :
          array[index_boucle], array[j] = array[j], array[index_boucle]
          index_boucle = depart
          j = index_boucle + 1
        else :
          j += 1
      index_boucle += 1
    return array
  elif (depart > fin) :
    while (index_boucle > fin_boucle) :
      j = index_boucle - 1
      while (j > fin_boucle) :
        if (array[j] > array[index_boucle]) :
          array[index_boucle], array[j] = array[j], array[index_boucle]
          index_boucle = depart
          j = index_boucle - 1
        else :
          j -= 1
      index_boucle -= 1
    return array
  else :
    return array

def tri_simple(array) :
  return tri(array, 0, int(len(array)))

def tri_arriere(array) :
  return tri(array, int(len(array) - 1), - 1)

def tri_milieu_vers_debut_fin(array) :
  y = len(array)
  x = int(y / 2)
  tri(array, x, 0)
  tri(array, x, y)
  return tri(array, 0, y)

def tri_debut_fin_vers_milieu(array) :
  a = len(array)
  b = int(a / 2)
  tri(array, 0, b)
  tri(array, a - 1, b)
  return tri(array, 0, a)

Algo_TS = Algorithme('Algorithme_Tri_Simple', tri_simple)
algos.append(Algo_TS)
Algo_AR = Algorithme('Algorithme_Tri_Arrière', tri_arriere)
algos.append(Algo_AR)
Algo_M_DF = Algorithme('Algorithme_Tri_Milieu_Vers_Début_Fin', tri_milieu_vers_debut_fin)
algos.append(Algo_M_DF)
Algo_DF_M = Algorithme('Algorithme_Tri_Début_Fin_Vers_Milieu', tri_debut_fin_vers_milieu)
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
