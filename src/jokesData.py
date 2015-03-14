"""
The jokes data repository !
Usage is simple : Just do a from jokesData import * and you can use the jokes list.
"""

import random

global jokes

jokes = []

"""
Reads the jokes dataset file and stores it in a list.
"""
def initJokesData():
    global jokes
    fileHandle = open('../jokesDataSet.txt','r')
    jokesData = fileHandle.read()
    jokes = jokesData.split("-------")
    fileHandle.close()

"""
Returns a random joke from the dataset.
"""
def getRandomJoke():
    global jokes
    numOfJokes = len(jokes)
    randomJoke = jokes[random.randint(0,numOfJokes-1)]
    return randomJoke
    
#This guy is important. This call initializes the list.
initJokesData()