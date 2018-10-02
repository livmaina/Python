As part of this assignment, please create a function randInt() where

randInt() returns a random integer between 0 to 100
randInt(max=50) returns a random integer between 0 to 50
randInt(min=50) returns a random integer between 50 to 100
randInt(min=50, max=500) returns a random integer between 50 and 500
Create this function without using random.randInt() but you are allowed to use random.random().

import random

def randInt():
    print(randInt(random.random()*100))  #up to 100
randInt()

def randInt(max=50):
    print(randInt(random.random()*50))   #up to 50
randInt()

def randInt(min=50):
    print(randInt(random.random()*50)+50) #50 to 100
randInt()

def randInt(min=50, max=500):
    print(randInt(random.random()*450)+50) #50 to 500
randInt()
