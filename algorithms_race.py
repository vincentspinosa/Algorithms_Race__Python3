# -*- coding: utf-8 -*-

from random import randint
import time
import gc

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
    for _ in range(self.input) :
      x = int(randint(1, 100000))
      self.array.append(x)
    print(f"L'array contient {self.input} valeurs à trier !")
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
      print(algos[i].nom)
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

def tri_primitif(array, a, b):
  while a < b:
    i = a + 1
    j = a
    while i < b:
      if(array[i] < array[a]):
        array[i], array[a] = array[a], array[i]
        a = j
        i = a + 1
      else:
        i += 1
    a += 1
  return array

def tri(array, depart, fin) :
  if (depart < fin) :
    return tri_primitif(array, depart, fin)
  elif (depart > fin) :
    return tri_primitif(array, fin, depart)
  else :
    return array

def tri_simple(array) :
  return tri(array, 0, int(len(array)))

def tri_arriere(array) :
  return tri(array, int(len(array)), - 1)

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

Algo_TS = Algorithme('Algorithme de Tri Simple', tri_simple)
Algo_AR = Algorithme('Algorithme de Tri Arrière', tri_arriere)
Algo_M_DF = Algorithme('Algorithme de Tri Milieu Vers Début Puis Fin', tri_milieu_vers_debut_fin)
Algo_DF_M = Algorithme('Algorithme de Tri Début et Fin Vers Milieu', tri_debut_fin_vers_milieu)

def appendToList(classe, array):
  for obj in gc.get_objects():
    if isinstance(obj, Algorithme):
      algos.append(obj)
  return None

appendToList(Algorithme, algos)


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
