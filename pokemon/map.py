import random
mapcoor = [[""]*10 for i in range (0,10)]
x=0
y=0
before = 0
def read ():
    global before
    i=0
    file = open("pokemon.txt", "r")
    for line in file:
        if (len(line) > 5):
            raw = line.split(" ")
            raw[7]=int(raw[7])
            raw[7]=str(raw[7])
            for p in range (0,8):
                mapcoor[i][p]=raw[p]
            i = i + 1
        else :
            before = line[0]
    file.close()
read()
def pmaps():
    global x,y
    for i in range (0,8):
        for p in range (0,8):
            if (mapcoor[i][p]== "0"):
                print ("0",end = " ")
            elif (mapcoor [i][p] == "1"):
                print ("x",end = " ")
                x=i
                y=p
            elif (mapcoor [i][p] == "2"):
                print ("#",end =" ")
        print ()
def write():
    files= open("pokemon.txt","w")
    temp =""
    for i in range (0,8):
        for p in range (0,8):
            temp = temp + mapcoor[i][p]
            if (p != 7):
                temp = temp +' '
            else :
                temp = temp + "\n"
    temp = temp + before
    files.write(temp)
    files.close
while 1:
    pmaps()
    print (x,y)
    print("=================")
    print("       MENU      ")
    print("=================")
    print("[1] Move up")
    print("[2] Move down")
    print("[3] Move left")
    print("[4] Move right")
    print("[5] Save & End Game")

    c = input("Input your choice:")
    if c=="1":
        if (x != 0):
            if (mapcoor[x-1][y]=="2"):
                counter = random.randint(0,1)
                if counter:
                    print ("encounter")
            mapcoor[x][y] = before
            x = x - 1
            before=mapcoor[x][y]
            mapcoor[x][y] = "1"
        else :
            print ("you cant")
    elif c=="2":
        if (x != 7):
            if(mapcoor[x+1][y]=="2"):
                counter = random.randint(0,1)
                if counter :
                    print("encounter")
            mapcoor[x][y] = before
            x = x + 1
            before=mapcoor[x][y]
            mapcoor[x][y] = "1"
        else :
            print("you cant")
    elif c=="3":
        if (y != 0):
            if (mapcoor[y-1][x]=="2"):
                counter = random.randint(0,1)
                if counter:
                    print ("encounter")
            mapcoor[x][y] = before
            y = y - 1
            before=mapcoor[x][y]
            mapcoor[x][y] = "1"
        else :
            print ("you cant")
    elif c=="4":
        if (y != 7):
            if (mapcoor[y+1][x]=="2"):
                counter = random.randint(0,1)
                if counter:
                    print ("encounter")
            mapcoor[x][y] = before
            y = y + 1
            before=mapcoor[x][y]
            mapcoor[x][y] = "1"
        else :
            print ("you cant")
    elif c=="5":
        write()
        break