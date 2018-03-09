#Commands: Look around, inspect, take, pick up, go west, east, north and south, climb, descend look left and right, go forward, backwards left and right
#Created by Joar and Johan, started 08 march 2018
#Fiara text game
#sys.exit()
import time
#Defining all the classes:
#Classes är global. Que?
c, r = 5, 3 #Number of tags, number of classes.
classes = [[0 for x in range(c)] for y in range(r)] #Hittade koden på stack overflow (tror jag). Fattar inte 100% hur den funkar, men rätt användbar.
#classes[0] is one class, [1] another etc.
classes[0][0] = "Mage" #Name of the class, placeholder
classes[0][1] = 10 #Attack damage/points, placeholder value.
classes[0][2] = 20 #Magic damage/points, placeholder value.
classes[0][3] = 25 #Armor, placeholder value.
classes[0][4] = 100 #Health, placeholder value.
classes[1][0] = "Warrior" #Name of the class, placeholder.
classes[1][1] = 25 #Attack damage/points, placeholder value.
classes[1][2] = 5 #Magic damage/points, placeholder value.
classes[1][3] = 50 #Armor, placeholder value.
classes[1][4] = 130 #Health, placeholder value.
classes[2][0] = "Priest" #Name of the class, placeholder.
classes[2][1] = 15 #Attack damage/points, placeholder value.
classes[2][2] = 20 #Magic damage/points, placeholder value.
classes[2][3] = 25 #Armor, placeholder value.
classes[2][4] = 150 #Health, placeholder value.
print("Text based Game Name, 2018 created by Joar and Johtli")
#import sys
#clueless = 0 clueless i room = "start" är odefinerat. man måste definera i varje rum.
inventory = []
rooms = [] #Lista med de senaste rummet man var i, så att man ska kunna skriva "go back" så går man till det rummet. rooms[1] är det förre rummet man var i.
allrooms = [] #Lista med alla rum man har varit i.
def handle_room(room):
        #global inventory
        if room == "start":
                clueless = 0
                if "Kerosene Lamp" in inventory:
                        print ("The dark room is lit up by the lamp you picked up.")
                else:
                        print ("The room is dark. You see a lamp in an adjacent room.")
                while True:
                        action = input("What will you do? \n")
                        action = action.lower()
                        if action == "look around":
                                #When you look around this happens
                                print ("You look around. The eerie silence crushes your eardrums. \
You are standing in a stone room made of bricks.\n\n\
There is a sockdrawer in the corner. The light in the other room seems miles away. \n")
                        elif "light" in action or "room" in action or "lamp" in action:
                                return "light"
                                #breaking the loop and you walk into the next room
                        elif "sockdrawer" in action:
                                print ("You approach the mystical drawer. It gives of an aura of adventure.")
                                #Princess bride easter egg which will affect the story later
                                while True:
                                        action = input ("What will you do?\n")
                                        action = action.lower()
                                        drawer = "closed"
                                        if "open" in action:
                                                print ("You listen to the voices in your head and open the drawer. Inside you find a book, titled 'The Princess Bride'.")
                                                time.sleep(2)
                                                print ("\nTantalized, you open it and read the first passage you see:")
                                                print ("Fencing, fighting, torture, revenge, giants, monsters, chases, escapes, true love and miracles!\n") #Kanske ta bort \n, få se.
                                                print ("It seems oddly relevant to your situation.")
                                                drawer = "open"
                                        elif drawer == "open":
                                                if "The Princess Bride" not in inventory:
                                                        if "take" in action:
                                                                print("The book is now in your satchel.") #to give a response to that action
                                                                inventory.append("The Princess Bride.")
                                                else:
                                                        if "take" in action:
                                                                print ("There is nothing to take.")
                                        elif "inspect" in action or "look" in action:
                                                print ("You take a closer look at the drawer. Seems like an ordinary sockdrawer, made of dark oak and passed down through generations. It reminds you of times past.")
                                        else:
                                                print ("You lose intrest and take a step back.") #Instead of this, have so id you misstype it prints "seems like you have lost intrest. perhaps you shouold take a step back.
                                                break
                        elif "back" in action:
                                if rooms[1] == "light":
                                        print ("You head back to the room you were in before.")
                                        return "light"
                        else:
                                print("Huh, that didn´t do anything")
                                if clueless == 3:
                                        print("You suddenly feel the urge to look around. Express the urge!")
                                elif clueless >= 4 and clueless <= 10:
                                        print("Express the urge")
                                elif clueless >= 10:
                                        print("Normal human behavior is: looking around, inspecting different objects and walking in different directions")
                                        print ("Write something sensible.")
                                clueless += 1
        elif room == "light":
                #Tog bort variabeln "light", onödig om man lägger till lampan till inventory.
                clueless = 0
                look = "no"
                taken = "no"
                if "Kerosene Lamp" in inventory and taken == "yes":
                        print ("There is nothing in the room.")
                elif "Kerosene Lamp" in inventory and taken != "yes":
                        print ("The room that was once lit up by the kerosene lamp is now only lit up by three glowing stones.")
                else:
                        print("Ten short steps and the light is in your reach. The light comes from a kerosene lamp.")
                while True:
                        action = input("What will you do? \n")
                        action = action.lower()
                        if action == "look around":
                                if taken == "no":
                                        print("This room has three glowing stones with the colours blue, red and white, \
lying on a flying pig. The pig looks happy but is stuck in the air by an unknown force.\n")
                                        print ("There is a door opposite to the dark room. The door seems closed.")
                                        
                                elif taken == "yes" and "Kerosene Lamp" not in inventory:
                                        print ("You look around. The room is lit up by a kerosene lamp.")
                                        print ("The only things appart from taht are two doors, one leading to the dark room and one leading to a pitch black hallway.")
                                        
                        elif "dark room" in action:
                                print ("You go into the dark room.")
                                return "start"
                        elif "back" in action:
                                if rooms[1] == "start":
                                        print ("You go back into the dark room.")
                                        return "start"
                        elif "pet" in action and "pig" in action:
                                if taken == "no":
                                        print("The pig seems pleased and oinks happily.")
                                elif taken == "yes":
                                        print ("The pig is gone. You cannot pet it anymore.")
                        elif action == "inspect":
                                print ("You inspect the dust in the air.")
                        elif "pick" in action and "up" in action and "light" in action or "pick" in action and "up" in action and "lamp" in action:
                                if "Kerosene Lamp" not in inventory:
                                        print("You pick up the light.")
                                        inventory.append("Kerosene Lamp") #Adds Kerosene Lamp to inventory.
                                else:
                                        print ("You have already picked up the light.")
                        elif "take" in action and "lamp" in action or "take" in action and "light" in action:
                                if "Kerosene Lamp" not in inventory:
                                        print("You pick up the light.")
                                        inventory.append("Kerosene Lamp")
                                else:
                                        print ("You have already picked up the light.")
                        elif "inspect" in action and "stone" in action or "take" in action and "stone" in action or "pick" in action and "stone" in action:
                                if "Mystic Stone" in inventory or "Holy Stone" in inventory or "Fierce Stone" in inventory:
                                        print ("The stones are no longer there to interact with.")
                                else:
                                        print("You touch the stones. \n\
The blue stone shows you a vision of stars and it feels like you are in a completely different world. \n\
The white stone makes you believe that you are the chosen and your faith is strong.\n\
The red stone makes you visualize your strenght and brute force. You feel strong.")
                                        stone = input("\n\nPick up a stone of your chosing. \n") #Which stone you pick up.
                                        stone = stone.lower()
                                        while True:
                                                if "blue" in stone:
                                                        print ("You take the blue stone and put it in your satchel.")
                                                        proffession = classes[0] #Your proffession (class) becomes classes[0].
                                                        inventory.append("Mystic Stone")
                                                        break
                                                elif "white" in stone:
                                                        print ("You take the white stone and put it in your satchel.")
                                                        proffession = classes[2]
                                                        inventory.append("Holy Stone")
                                                        break
                                                elif "red" in stone:
                                                        print ("You take the red stone and put it in your satchel.")
                                                        proffession = classes[1]
                                                        inventory.append("Fierce Stone")
                                                        break
                                                else:
                                                        print("Pick a stone of your chosing")
                                        print("Just as you take the stone off the pig's back, the other stones vanish. You hear a clicking sound from the door.")
                        elif "enter" in action or "door" in action:
                                return "hallway"
                        else:
                          if look == "no":
                                print("Huh that didn´t work.") #to atleast give som response
                                clueless += 1
                                if clueless == 3:
                                        print("You suddenly feel the urge to look around. Express the urge!")
                                elif clueless >= 4 and clueless <= 10:
                                        print("Express the urge")
                                elif clueless >= 10:
                                        print("Normal human behavior is: looking around, inspecting different objects and walking in different directions")
                          else:
                                if clueless < 3:
                                        print ("Huh, that didn't work.")
                                else:
                                        print("Normal human behavior is: looking around, inspecting different objects and walking in different directions")
                                        clueless += 1
        
        elif room == "hallway":
                print("Just as you approach it, the door creaks open.")
                time.sleep(1)
                if "Kerosene Lamp" in inventory:
                        print ("You take a step forwards to take a look, but suddenly the door slams shut! You're pushed into a hallway, \
illuminated only by your lamp. You can barely see the other end.")
                else:
                        print ("You take a step forwards to take a look, but suddenly the door slams shut! You're pushed into a pitch black hallway.")
                while True: 
                        action = input("What will you do? \n")
                        action = action.lower()
                        if "look" in action or "inspect" in action:
                                if "Kerosene Lamp" in inventory:
                                        print ("You notice an open trapdoor two steps infront of you. The cavity below is filled with spikes.\n")
                                        print ("Making sure you don't activate any other traps, you make your way to the other end of the corridor.")
                                        #Go to a new room, a body is on the ground. Take the items.
                                else:
                                        print ("You look around, but see nothing in the thick darkness.")#######
                        elif "forwards" in action:
                                if "Kerosene Lamp" in inventory:
                                        print("You step around the trapdoor, thanking your gods that you took the lamp when you had the chance.")
                                        #You make it to the end of the hallway, taking great care not to tread on any traps.
                                else:
                                        print("You feel a sudden, immense pain one moment and in the next, everything goes dark. \n\
Your journey has come to a tragic end")
                                        return "death"
        elif room == "death":
                print ("Restart")
        else:
                print ("Oops, room did not have a value. Returning to the last room you were in...")
                return rooms[1]
  	####
room = "start"
while room != "end":
        room = handle_room(room)
        rooms.insert(0,room)
        allrooms.append(room)
        if len(rooms) > 2:
                rooms.pop(2)
input("\n\nPress the Enter key to exit.")
