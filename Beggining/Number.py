import math  # This will import math module
print("math.ceil(-45.17) : ", math.ceil(-45.17))
print("math.ceil(100.12) : ", math.ceil(100.12))
print("math.ceil(100.72) : ", math.ceil(100.72))
print("math.ceil(math.pi) : ", math.ceil(math.pi))
print("math.floor(-45.17) : ", math.floor(-45.17))
print("math.floor(100.12) : ", math.floor(100.12))
print("math.log10(100.12) : ", math.log10(100.12))
print(" math .max:", max(88, 8, 0, 9))
print("math.modf(100.12) : ", math.modf(100.12))
print("math.pow(100, 2) : ", math.pow(100, 2))
print("round(70.23456) : ", round(70.23456))
print("math.sqrt(100) : ", math.sqrt(100))
print("acos(0.64) : ", math.acos(0.64))
print("asin(0.64) : ", math.asin(0.64))
print("atan(0.64) : ", math.atan(0.64))
print("atan2(-0.50,-0.50) : ", math.atan2(-0.50, -0.50))
print("cos(3) : ", math.cos(3))
print("hypot(3, 2) : ", math.hypot(3, 2))
print("sin(3) : ", math.sin(3))
print("tan(math.pi) : ", math.tan(math.pi))
print("degrees(-3) : ", math.degrees(-3))
print("radians(math.pi) : ", math.radians(math.pi))


import random
print("returns a random number from range(100) : ", random.choice(range(100)))
print("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1,
                                                                             2, 3, 5, 9]))
print("returns random character from string 'Hello World' : ",
      random.choice('Hello World'))
print("randrange(1,100, 2) : ", random.randrange(1, 100, 5))
# randomly select a number between 0-99
print("randrange(100) : ", random.randrange(100))
print("random() : ", random.random())
# Second random number
print("random() : ", random.random())
random.seed()
print("random number with default seed", random.random())
random.seed(10)
print("random number with int seed", random.random())
random.seed("hello", 2)
print("random number with string seed", random.random())
list = [20, 16, 10, 5];
random.shuffle(list)
print("Reshuffled list : ", list)
random.shuffle(list)
print("Reshuffled list : ", list)
print("Random Float uniform(5, 10) : ", random.uniform(5, 10))
print("Random Float uniform(7, 14) : ", random.uniform(7, 14))


from random import randint
print(randint(1, 9))

from random import choice
players =['charles','martina','micheal','florence''eli']
first_up=choice(players)
print(first_up)
