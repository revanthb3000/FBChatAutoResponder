"""
This guy stores all the conversations you're having right now and responds appropriately.
"""
from botResponsesAndStates import *
from jokesData import *
from utilityFunctions import *
import re
import utilityFunctions

global conversations 

conversations = {}

"""
Given a new message and the person who sent it, I either create a new mapping or add to the existing one.
"""
def addMessageToConversation(address, newMessage):
    global conversations
    if(isChatNew(address)):
        newDictionary = {"messages" : [newMessage], "state" : 0};
        conversations[address] = newDictionary
    else:
        conversations[address]["messages"].append(newMessage)
        
"""
This function checks if a chat is already in progress.
"""
def isChatNew(address):
    if(address in conversations.keys()):
        return False
    return True

"""
Changes the state of a conversation to a given value.
"""
def changeState(address, newState):
    if(address in conversations.keys()):
        conversations[address]["state"] = newState
        
"""
A basic utility function.
"""
def printConversations():
    global conversations
    for key in conversations.keys():
        print key + " ",
        print conversations[key]

"""
The core of this entire file. Given a message and an address, previous conversation is looked at and a response is generate.
"""
def getResponse(fromAddress, newMessage):
    global conversations
    addMessageToConversation(fromAddress, newMessage)
    userChat = conversations[fromAddress]
    if(userChat["state"]==BOT_START_STATE): #Means that the user is still in state 0.
        changeState(fromAddress, BOT_MAIN_MENU_STATE)
        return BOT_INTRO
    elif(userChat["state"]==BOT_MAIN_MENU_STATE):
        userMessageResponse = re.sub("[^0-9]","",newMessage)
        userMessageResponse = "0" + userMessageResponse
        if(int(userMessageResponse)==1):
            return BOT_OWNER_WHEARABOUTS + "\n" + BOT_ASK_FOR_RESPONSE
        elif(int(userMessageResponse)==2):
            return getRandomJoke() + "\n" + BOT_ASK_FOR_RESPONSE
        elif(int(userMessageResponse)==3):
            playAlert()
            return BOT_ALERT_RESPONSE + "\n" + BOT_ASK_FOR_RESPONSE
        elif(int(userMessageResponse)==4):
            changeState(fromAddress, BOT_STORY_MODE_START_STATE)
            return BOT_START_STORY + "\n" + utilityFunctions.getStoryNodeMessage(0)
        else:
            return BOT_INVALID_RESPONSE + "\n" + BOT_ASK_FOR_RESPONSE
    elif(userChat["state"] in BOT_STORY_MODE_STATE_RANGE):
        currentState = userChat["state"] - BOT_STORY_MODE_START_STATE #Getting rid of the offset
        
        userMessageResponse = re.sub("[^0-9]","",newMessage)
        userMessageResponse = int("0" + userMessageResponse)
        
        newState = 0
        if(userMessageResponse==1):
            newState = getNextState(currentState, 1)
        elif(userMessageResponse==2):
            newState = getNextState(currentState, 2)
        else:
            return BOT_INVALID_RESPONSE + "\n" + BOT_ASK_FOR_RESPONSE
        
        replyMessage = utilityFunctions.getStoryNodeMessage(newState)
        if(utilityFunctions.isEndState(newState)):
            #If we're gonna be going to an end state, then we might as well be going to the main menu.
            newState = BOT_START_STATE
        else:
            newState += BOT_STORY_MODE_START_STATE
        
        changeState(fromAddress, newState)
        
        return replyMessage
