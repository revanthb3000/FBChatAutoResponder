"""
I'm gonna put in the general purpose functions I use over here.
"""
import pygame
import time
from botResponsesAndStates import *

"""
Plays an alert sound.
"""
def playAlert():
    pygame.init()
    pygame.mixer.init()
    sounda= pygame.mixer.Sound("../alert.wav")
    
    sounda.play()
    time.sleep(23)

"""
Gets the message and options and puts them in a presentable format.
"""
def getStoryNodeMessage(storyNodeId):
    message = BOT_STORY_MESSAGES[storyNodeId] + "\n"
    options = BOT_STORY_OPTIONS[storyNodeId]
    cnt = 1
    for option in options:
        message += "\n" + str(cnt) + ". " + option
        cnt += 1
    return message

"""
Given an option, this node moves the story to the next branch.
"""
def getNextState(storyNodeId, optionId):
    nextStates = BOT_STORY_PATHS[storyNodeId]
    return nextStates[optionId-1]

"""
Check if the story has ended.
"""
def isEndState(storyNodeId):
    if(len(BOT_STORY_PATHS[storyNodeId])==0):
        return True
    else:
        return False