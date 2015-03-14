"""
This guy contains everything to do with connecting, sending, receiving messages. Basically everything your IM Client does.
"""

import xmpp
import conversationHandler
from clientParameters import *
import sleekxmpp
import logging

global chatbot
logging.basicConfig(level=logging.DEBUG)

def session_start(event):
    chatbot.send_presence()
    chatbot.get_roster()

def login():
    fileHandle = open(CREDENTIALS_FILENAME,'r')
    username = str(fileHandle.readline()).strip()
    password = str(fileHandle.readline()).strip()
    fileHandle.close()
    
    jid = username + '@chat.facebook.com'
    server = (FB_SERVER_NAME, FB_PORT_NUMBER)
    
    global chatbot
    chatbot = sleekxmpp.ClientXMPP(jid,password)
    chatbot.add_event_handler('session_start', session_start)
    chatbot.add_event_handler('message', handleMessage)
    chatbot.auto_reconnect = True
    chatbot.connect(server)
    chatbot.process(threaded=False)
    
"""
You get a message and you want to do something with it ? This is the function for you !
"""
def handleMessage(receivedMessage): 
    fromAddress = receivedMessage['from']
    messageBody = receivedMessage['body']
    if receivedMessage['type'] in ('chat','normal'):
        message = str(messageBody)
        responseMessage = conversationHandler.getResponse(str(fromAddress), message)
        conversationHandler.printConversations()
        receivedMessage.reply(responseMessage).send()
