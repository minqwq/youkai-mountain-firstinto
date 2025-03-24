import os
import sys
import time

while True:
    isWindowsPre = input("Are you using Windows?[Y/N] ")

    if isWindowsPre.lower() == "y":
        isWindows = True
        break
    elif isWindowsPre.lower() == "n":
        isWindows = False
        break

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
    os.system(sys.executable + " chapter/001.py")
elif mainchoice == "2":
    # TODO: 显示可用代码文件
    choice02 = input("select chapter: ")
    os.system(sys.executable + " chapter/" + choice02.rjust(3, "0") + ".py")
elif mainchoice == "3":
    cat("score/ranking.txt") # 这个可能是没有做
elif mainchoice == "5":
    sys.exit()


# 这里要是没按要求做会崩掉注意下