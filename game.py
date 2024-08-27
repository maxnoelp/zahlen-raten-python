import random
x = random.randrange(1, 250)
trys = 10


     
print("Willkommen beim ZahlenRatenSpiel!")
print("Gesucht wird eine Zahl zwischen 1 - 250!")
print("Du hast " + str(trys) + " versuche, um die Gesuchte Zahl zu erraten!")
print("Schreib hier deinen Namen, drück Enter und teil uns deine Schätzung mit!")
name = input()

while trys > 0:
    trys -= 1
    inpt = int(input())
    if inpt > x:
        print(name + ", die Gesuchte Zahl ist kleiner!")
        print("Du hast noch " + str(trys) + " übrig!")
    elif inpt < x:
        print(name + ", die Gesuchte Zahl ist größer!")
        print("Du hast noch " + str(trys) + " übrig!")
    elif inpt == x:
        print("Nice, " + name + " u got it! Deine verbleibende Versuche:"  + str(trys))  
        break
    if trys == 0:
        print("Schade, versuch es noch einmal!")
    
        