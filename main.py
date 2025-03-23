import os
import sys
import time

isWindowsPre = input("Are you windows?[Y/N] ")
if isWindowsPre == "Y" or isWindowsPre == "y":
    isWindows = True
elif isWindowsPre == "N" or isWindowsPre == "n":
    isWindows = False

def clearScreen():
    if isWindows == True:
        os.system("cls")
    elif isWindows == False:
        os.system("clear")

clearScreen()
print("Flandre Studio & mibino")
time.sleep(3)
clearScreen()
print("妖之山 Project 初探\nYoukai Mountain Project - First into mountain")
print("-- a Fighting game like rpg but its not rpg --")
mainchoice = input("\n1:Start\n2:Prac. Start\n3:Score Ranking\n4:Options\n5:Exit\nSelect choice >>> ")
if mainchoice == "1":
    os.system("python chapter/001.py")
elif mainchoice == "2":
    choice02 = input("select chapter: ")
    os.system("python chapter/00" + choice02 + ".py")
elif mainchoice == "3":
    cat("score/ranking.txt")
elif mainchoice == "5":
    sys.exit()
