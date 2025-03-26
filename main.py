import os
import sys
import time
import pygame
pygame.mixer.init()
pygame.mixer.music.load("./music/gf_01_01_03.mp3")
try:
    isWindows = sys.platform.startswith('win')

    isWindowsPre = input("Are you using Windows?[" + ("Y/n" if isWindows else "y/N") + "] ")

    if isWindowsPre.lower() == "y":
        isWindows = True
    elif isWindowsPre.lower() == "n":
        isWindows = False
    def clearScreen():
        if isWindows == True:
            os.system("cls")
        elif isWindows == False:
            os.system("clear")

    clearScreen()
    print("Flandre Studio & mibino")
    time.sleep(3)
    while True:
        pygame.mixer.music.play()
        clearScreen()
        print("妖之山 Project 初探")
        print("Youkai Mountain Project - First into mountain")
        print("-- a Fighting game like rpg but its not rpg --")
        print()
        print("1:Start")
        print("2:Prac. Start")
        print("3:Score Ranking")
        print("4:Options")
        print("5:Exit")
        mainchoice = input("Select choice >>> ")
        if mainchoice == "1":
            exec(open(os.path.dirname(os.path.abspath(__file__)) + os.sep + "chapter" + os.sep + "001.py", encoding="utf-8").read())
        elif mainchoice == "2":
            # TODO: 显示可用代码文件
            choice02 = input("select chapter: ")
            exec(open(os.path.dirname(os.path.abspath(__file__)) + os.sep + "chapter" + os.sep + choice02.rjust(3, "0") + ".py", encoding="utf-8").read())
        elif mainchoice == "3":
            cat("score/ranking.txt") # 这个可能是没有做
        elif mainchoice == "5":
            sys.exit()
except EOFError:
    print("EOFError强制退出游戏")
    sys.exit(1)
except KeyboardInterrupt:
    print("强制中断")
    sys.exit(1)

# 这里要是没按要求做会崩掉注意下
