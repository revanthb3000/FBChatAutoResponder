"""
This file contains all the responses that will be given by the bot.
"""

BOT_INTRO = "Hey there ! I'm a bot who's taking the place of my owner who's not here right now. "\
                "How may I entertain you ? \n"\
                "1. Where's the Goddamn owner ?!\n"\
                "2. Tell me a joke.\n"\
                "3. Sound off an alert to grab my owner's attention.\n"\
                "4. Wanna play a game ?"
                
BOT_OWNER_WHEARABOUTS = "I don't know :( He doesn't tell me anything. I'm used as a tool."

BOT_ALERT_RESPONSE = "Okay. I've sounded off an alert that might grab my owner's attention. You're welcome !"

BOT_INVALID_RESPONSE = "Please enter a valid response (one of the options). I'm not smart enough."

BOT_ASK_FOR_RESPONSE = "Enter an option : "

BOT_START_STORY = "Lets start playing then !"

BOT_STORY_MESSAGES = ["You just wake up and feel hazy. It's completely dark and you can barely see anything except a door in front of you (with the handle placed to the right). "
                    + "There's also a small window that seems to be connected to the other room from which you hear voices. They're probably the kidnappers. "
                    + "You can't move your feet. They seem to be tied up. Your hands are bound too but the rope doesn't seem to be that strong. What do you do ?",
                    
                      "You use a bit of force and shake off the knot tying your hands down. Getting rid of the knot tying your legs to the chair is now straightforward. "
                    + "You do so and stand up. You move toward the door and try to open it. As expected, its locked. You observe what's in the room. "
                    + "On the right you see a switchboard with a single switch that probably controls the big lamp in the center of the room. "
                    + "On the left you see a briefcase. Which way will you go ?",
                    
                      "You move towards the switchboard and flip the switch. The lamp turns on. It dazzles you for a minute. It is brighter than you expected. "
                    + "You hear the kidnappers shout. They've noticed the light. You hear footsteps. They're coming !! What do you do ?",
                    
                      "You immediately switch off the light but by the time you get the chance to hide, they barge in and shoot. You get shot in the stomach and go down. "
                    + "The kidnappers argue for a while on what to do with you. They decide to lock the door and let you rot inside. You eventually die of blood loss.",
                            
                      "You go towards the briefcase in the corner. It appears familiar and seems to be something that belongs to you. You have to enter a three digit code to unlock it. "
                    + "You're woozy and can't remember exactly what the lock-code was. It's either 212 or 121. Your mind has thoughts - 'first..3 digits....drome'?! What do you enter ? ",

                      "Excellent ! The code is correct and you are able to unlock the briefcase. To your horror, you find a revolver in it and nothing else.  "
                    + "This startles you causing you to drop the briefcase. The kidnappers hear it and are running towards the room. What do you do ?",
                    
                      "You enter the wrong code and the lock-systems makes a beep sound that startles you and causes you to drop the briefcase. "
                    + "The kidnappers hear it and are running towards the room. What do you do ?",
                    
                      "You stand your ground and wait for the kidnappers to come in. They open the door and you pull the trigger. No bullet is fired. The bullet chamber was empty."
                    + "You spin the cylinder and try again but before you can pull the trigger, you get shot. You drop the revolver and clutch your arm. They approach you. "
                    + "One of the kidnappers kicks the revolver away. The other holds his pistol to your head. BOOM ! In one moment, you've lost your life. You are dead.",
                    
                      "You decide to hide near the door. Which side ?",
                      
                      "You go hide to the left of the door. The kidnappers push open the door and the toruque effect causes you to get hit by the door. "
                    + "You fall to the ground and almost lose consciousness. By the time you get up, the kidnappers have spotted you. "
                    + "One of the kidnappers smacks you with the butt of his pistol. You become woozy and fall down. Blood drips from your forehead. "
                    + "The kidnappers continue to assault you till you pass out and die due to blood loss. You are dead.",
                            
                      "You go to the right of the door. The kidnappers open the door and head towards the center of the room. "
                    + "They don't notice you. Now's your chance ! What do you do ?",
                    
                      "You try to jump on one of the kidnappers. You both fall to the ground and struggle. Sadly, the other kidnapper joins in and overpowers you, throwing you away. "
                    + "While you struggle to get up, he grabs his pistol and lands a headshot. You are dead.",
                    
                      "You manage to leave the room and lock the door. The kidnappers are trapped. They keep shouting and threaten you but its immaterial. They're the ones that are trapped now ! You WIN !!",
                      
                      "You scream at the top of your lungs. The kidnappers hear you. They approach the window and warn you to not do that again. What do you do now ?",
                      
                      "You try screaming again. One of the kidnappers get ticked off and enter the room. He places his gun to your head and pulls the trigger. You are dead."
                      
                    ]

BOT_STORY_OPTIONS = [["Use a bit of force and try to untie your hands.","Scream"],
                     ["Go to the switchboard.","Go to the briefcase."],
                     ["Switch off the light and try to hide.","Attack the kidnappers head on !"],
                     [],
                     ["212","121"],
                     ["Attack the kidnappers head on ! You have a gun !","Hide near the door."],
                     ["Hide near the door.","Attack the kidnappers head on !"],
                     [],
                     ["Left","Right"],
                     [],
                     ["Jump on the kidnappers. They have their backs turned against you.","Leave the room and try to lock the door."],
                     [],
                     [],
                     ["Use a bit of force and try to untie your hands.","Scream"],
                     []]

BOT_STORY_PATHS = [[1,13],
                   [2,4],
                   [3,11],
                   [],
                   [6,5],
                   [7,8],
                   [8,11],
                   [],
                   [9,10],
                   [],
                   [11,12],
                   [],
                   [],
                   [1,14],
                   []]

"""
Put in all the states down below
"""
BOT_START_STATE = 0
BOT_MAIN_MENU_STATE = 1
BOT_STORY_MODE_START_STATE = 2
#There are 15 story nodes and so everything from 2 to 16 count as story nodes.
BOT_STORY_MODE_STATE_RANGE = range(2,17)
