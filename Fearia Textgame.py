#Commands: Look around, inspect, take, pick up, go west, east, north and south, climb, descend look left and right, go forward, backwards left and right
#Created by Joar and Johan, started 08 march 2018
#Fiara text game
#sys.exit()
import time
#Defining all the classes:
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
def handle_room(room):
        if room == "start":
                clueless = 0
                print ("The room is dark, you see a candle standing in an adjacent room.")
                while True:
                        action = input("What will you do? \n")
                        action = action.lower()
                        if action == "look around":
                                #When you look around this happens
                                print ("You look around. The eerie silence crushes your eardrums. \
You are standing in a stone room made of bricks.\n\n\
There is a sockdrawer in the corner. The light in the other room seems miles away. \n")
                        elif "light" in action or "other room" in action:
                                return "light"
                                #breaking the loop and you walk into the next room
                        elif "sockdrawer" in action:
                                print ("You approach the mystical drawer. It gives of an aura of adventure.")
                                #Princess bride easter egg which will affect the story later
                                while True:
                                        action = input ("What will you do?\n")
                                        action = action.lower()
                                        if "open" in action:
                                                print ("You listen to the voices in your head and open the drawer. Inside you find a book, titled 'The Princess Bride'.")
                                                time.sleep(2)
                                                print ("\nTantalized, you open it and read the first passage you see:")
                                                print ("Fencing, fighting, torture, revenge, giants, monsters, chases, escapes, true love and miracles!\n") #Kanske ta bort \n, få se.
                                                print ("It seems oddly relevant to your situation.")
                                        elif "take" in action:
                                                print("The book is now in your satchel") #to give a response to that action
                                        elif "inspect" in action or "look" in action:
                                                print ("You take a closer look at the drawer. Seems like an ordinary sockdrawer, made of dark oak and passed down through generations. It reminds you of times past.")
                                        else:
                                                print ("You lose intrest and take a step back.")
                                                break
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
                clueless = 0
                print("Ten short steps and the light is in your reach. The light comes from a kerosene lamp.")
                while True:
                        action = input("What will you do? \n")
                        action = action.lower()
                        if action == "look around":
                                print("This room has three glowing stones with the colours blue, red and white \
lying on a flying pig. The pig looks happy but is stuck in the air by an unknown force") #Lägg till mer beskrivning. #Gjort!
                        elif "pet" in action and "pig" in action:
                                print("The pig seems pleased and oinks happily.")
                        elif action == "inspect":
                                print ("You inspect the dust in the air.")
                        elif "pick" in action and "up" in action and "light" in action:
                                global light
                                light = "picked up"
                                print("You pick up the light")
                        elif "pick" in action and "up" in action and "lamp" in action:
                                light = "picked up"
                                print("You pick up the light")
                        elif "pick" in action and "up" in action and "kerosene lamp" in action:
                                light = "picked up"
                                print("You pick up the light")
                        elif "inspect" in action and "stone" in action: #Add pick up stones, take stones, inspect stones.
                                ####You should only be able to take the stone if you have not already. do if stone == "untaken":
                                #Maybe a brief presentation of the stones instead, and the only vision you see is the one of the stone you took?
                                print("You touch the stones. \n\
             The blue stone shows you a vision of stars and it feels like you are in a completely different world. \n\
             The white stone makes you belive that you are the chosen and your faith is strong.\n\
             The red stone makes you visualize your strenght and brute force. You feel strong.")
                                stone = input("\n\nPick up a stone of your chosing. \n") #Which stone you pick up.
                                stone = stone.lower()
                                while True:
                                        if "blue" in stone:
                                                print ("You take the blue stone.")
                                                proffession = classes[0] #Your proffession (class) becomes classes[0].
                                                break
                                        elif "white" in stone:
                                                print ("You take the white stone.")
                                                proffession = classes[2]
                                                break
                                        elif "red" in stone:
                                                print ("You take the red stone.")
                                                proffession = classes[1]
                                                break
                                        else:
                                                print("Pick a stone of your chosing")
                                print("Just as you take the stone of the pig the other stones wanishes and a door opens.")
                         elif "open" in action and "door" in action:
                                return "Hallway"
                       
                                
    		

                        else:
                                print("Huh that didn´t work.") #to atleast give som response
                                clueless += 1
                                if clueless == 3:
                                        print("You suddenly feel the urge to look around. Express the urge!")
                                elif clueless >= 4 and clueless <= 10:
                                        print("Express the urge")
                                elif clueless >= 10:
                                        print("Normal human behavior is: looking around, inspecting different objects and walking in different directions")
        
        elif room == "Hallway":
                print("The door opens but when you look inside the next room it slams you into a dark hallway.")
                while True: 
                        action = input("What will you do? \n")
                        action = action.lowercase
                        if light == "picked up":
                                print("Because of the kersosene lamp you see a trap door.")
                        ####elif light =! "picked up":
                                #print("You feel a great pain one moment and in the next, everything goes dark. \n\
#Suddenly your journey has ended")
                                #start over game
  	####
room = "start"
while room != "end":
  room = handle_room(room)
  
input("\n\nPress the Enter key to exit.")
