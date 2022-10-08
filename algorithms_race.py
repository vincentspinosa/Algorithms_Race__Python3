from random import randint
import time
import gc


#TIMING THE FUNCTION:

class Time:
  def __init__(self, function, function_param):
    t1 = time.time()
    function(function_param)
    t2 = time.time()
    self.result = t2 - t1
    return None

  def __repr__(self):
    return f"Result: {self.result}"


#ALGORITHM: (definition)

class Algorithm:
  def __init__(self, name, function):
    self.name = name
    self.function = function
    return None

  def __repr__(self):
    return f"Algorithm: {self.name}, Function: {self.function}"

algos = []


#RACE: (definition)

class Init:
  def __init__(self):
    try:
      inpt = int(input('\nEnter the number of values contained in the array (150 by default, min 2, max 1200): '))
    except ValueError:
      inpt = 150
    if (inpt < 2):
      inpt = 2
    elif (inpt > 1200):
      inpt = 1200
    self.input = inpt
    self.array = []
    i = 0
    for _ in range(self.input):
      x = int(randint(1, 100000))
      self.array.append(x)
    print(f"The array contains {self.input} values to sort!")
    return None

  def __repr__(self):
    return f"Input: {self.input}\nArray: {self.array}"

class Race:
  def __init__(self):
    a = Init()
    arrayCpy = a.array.copy()
    i = 0
    current_best = None
    for i in range(len(algos)):
      print(f"\n{algos[i].name}")
      print(f"Array to sort: {a.array}")
      print("Sorting in progress...")
      result = Time(algos[i].function, a.array).result
      print(f"Result: {a.array}")
      a.array = arrayCpy.copy()
      print(f"Time of {algos[i].name}: {result}")
      if (current_best == None or result < current_best):
        current_best = result
        best_algo = [algos[i].name]
      elif (current_best == result):
        best_algo.append(algos[i].name)
    self.winner = best_algo
    self.best_time = current_best
    print(f"\n{self.winner} wins with a time of {self.best_time}!")
    New_Race()
    return None

  def __repr__(self):
    return f"Winner: {self.winner} \nBest time: {self.best_time}"

class New_Race:
  def __init__(self):
    print("\nDo you want to do a new race?")
    print("1: Yes")
    print("2: No")
    try:
      self.ipt = int(input("\nEnter the value corresponding to the desired action: "))
    except ValueError:
      self.ipt = 3
    if (self.ipt == 1):
      Race()
    elif (self.ipt == 2):
      print("\nSee you soon!")
    else:
      New_Race()
    return None

  def __repr__(self):
    return f"Chosen option: {self.ipt}"


#ALGORITHMS:

def primitive_sort(array, a, b):
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

def sort(array, start, end):
  if (start < end):
    return primitive_sort(array, start, end)
  elif (start > end):
    return primitive_sort(array, end, start)
  else:
    return array

def simple_sort(array):
  return sort(array, 0, int(len(array)))

def reverse_sort(array):
  return sort(array, int(len(array)), - 1)

def sort_middle_to_start_end(array):
  y = len(array)
  x = int(y / 2)
  return sort(sort(sort(array, x, 0), x, y), 0, y)

def sort_start_end_to_middle(array):
  x = len(array)
  y = int(x / 2)
  return sort(sort(sort(array, 0, y), x - 1, y), 0, x)

Algo_SS = Algorithm('Simple Sort Algorithm', simple_sort)
Algo_RS = Algorithm('Reverse Sort Algorithm', reverse_sort)
Algo_M_SE = Algorithm('Sort Middle to Start, then Middle to End, then All', sort_middle_to_start_end)
Algo_SE_M = Algorithm('Sort Start to Middle, then End to Middle, then All', sort_start_end_to_middle)

def appendToList(class_, array):
  for i in gc.get_objects():
    if isinstance(i, class_):
      array.append(i)
  return None

appendToList(Algorithm, algos)


#WELCOME:

def welcome():
  print("Welcome to the algorithms' race!")
  print("In this game, several algorithms race to sort an array the fastest.")
  print("It will be up to you, the user, to indicate the number of values contained in the array to sort.")
  return None


#MAIN:

def main():
  welcome()
  Race()
  return None


#RACE:

main()
