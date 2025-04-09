# THIS IS A DEMO VERSION AND NOT ARE THE RELEASE VERSION EXPRIENCE
# Flandre Studio 20250326
# Copyright (c) 2025 minqwq, wusheng233

import pygame
import os
import sys
import json
import random
import time
from module.actions import *

def runSubProgram(pathtoapp):
    if isWindows == "true":
        os.system("python " + pathtoapp)
    elif isWindows == "false":
        if venvEnable == "true":
            if replace_python_command_to_python3 == "true":
                os.system(venvPath + "3 " + pathtoapp)
            elif replace_python_command_to_python3 == "false":
                os.system(venvPath + " " + pathtoapp)
            else:
                print("Config incorrect at \"replace_python_command_to_python3\"")
                print("check it on config/conf.json\nif you need help please contact minqwq723897@outlook.com")
                sys.exit()
        else: # too --minqwq
            if replace_python_command_to_python3 == "true":
                os.system("python " + pathtoapp)
            elif replace_python_command_to_python3 == "false":
                os.system("python3 " + pathtoapp)
            else:
                print("Config incorrect at \"replace_python_command_to_python3\"")
                print("check it on config/conf.json\nif you need help please contact minqwq723897@outlook.com")
                sys.exit()

class Chapter1:
    VERSION = "Preview 0.03a"
    gameconfig = {}
    sounds = {}
    curyoukai = {}
    gamedir = ""
    playerhealth = 3500
    gamescore = 0
    overdrives = 0
    overdrivemode = False
    spells = 0
    gamedevmode = False
    yourName = ""
    # remainYoukais = 20
    boss = [
        {"name": "Eduarte", "defend": 4, "attack": {"start": 90, "stop": 180}, "health": 3000}
    ]
    tiny_youkais = [
        {"name": "大妖精", "defend": 1.2, "attack": {"start": 80, "stop": 120}, "health": 2000},
        {"name": "琪露诺", "defend": 1.09, "attack": {"start": 9, "stop": 99}, "health": 1999},
        {"name": "幽灵", "defend": 2, "attack": {"start": 1, "stop": 50}, "health": 1000},
        {"name": "不保存姐", "defend": 1, "attack": 1, "health": 1},
        {"name": "小女仆", "defend": 1.4, "attack": {"start": 40, "stop": 130}, "health": 1500},
        {"name": "小妖精", "defend": 1.1, "attack": {"start": 40, "stop": 60}, "health": 1000}
    ]
    weapons = [
        {"name": "生锈到快断掉的刀", "damage": {"start": 50, "stop": 160}, "overdrive": False, "broken": {"stop": 20, "msg": "刀断了..."}},
        {"name": "锤ta", "damage": {"start": 70, "stop": 100}, "overdrive": {"start": 150, "stop": 270}, "broken": False},
        {"name": "脚踢", "damage": {"start": 80, "stop": 130}, "overdrive": {"start": 200, "stop": 350}, "broken": False},
    ]
    def __init__(self):
        self.yourName = ""
        self.gamedir = os.path.dirname(os.path.abspath(__file__)) + os.sep
        self.gameconfig = json.load(open(self.gamedir + "config.json", "r", encoding="utf-8"))
        self.overdrives = int(self.gameconfig["overdrives"])
        self.spells = int(self.gameconfig["spells"])
        self.gamedevmode = self.gameconfig["devmode"] == "true"
        self.venvEnable = self.gameconfig["venvEnable"]
        self.venvPath = self.gameconfig["venvPath"]
        self.replace_python_command_to_python3 = self.gameconfig["replace_python_command_to_python3"]
        self.isWindows = self.gameconfig["isWindows"]
        self.remainYoukais = 5
        if self.gamedevmode:
            self.tiny_youkais.append({"name": "test", "defend": {"start": 0.5, "stop": 4.0}, "attack": {"start": 10, "stop": 200}, "health": {"start": 100, "stop": 3000}})
            self.weapons.append({"name": "test", "damage": 10, "overdrive": 20, "broken": False})
            self.weapons.append({"name": "brokentest", "damage": 1, "overdrive": 2, "broken": {"stop": 2, "msg": "OK"}})
            self.weapons.append({"name": "一刀9999", "damage": 9999, "overdrive": 99999, "broken": False})
            self.weapons.append({"name": "testNoOverdriveNoBroken", "damage": 68, "overdrive": False, "broken": False})
        pygame.mixer.init()
        pygame.mixer.music.load("music/gf01_02.mp3")
        pygame.mixer.music.play()
        self.loadSound("select00", "sfx/select00.wav")
        self.loadSound("nep00", "sfx/nep00.wav")
        self.loadSound("ok00", "sfx/ok00.wav")
        self.loadSound("extend", "sfx/extend.wav")
        self.loadSound("tan00", "sfx/tan00.wav")
        self.loadSound("pldead00", "sfx/pldead00.wav")
        self.randomChoice()
        self.mainLoop()
    def loadSound(self, name, path):
        self.sounds[name] = pygame.mixer.Sound(path)
    def playSound(self, name):
        self.sounds[name].play()
    def mainLoop(self):
        clearScreen()
        initialgamescore = self.gamescore
        if self.curyoukai["health"] <= 0: # FIXME: 有的时候血量变负值都没有触发死亡
            self.playSound("pldead00")
            self.playerhealth += self.curyoukai["health"] / 8 + 350
            self.randomChoice()
        if self.playerhealth <= 0:
            self.playSound("pldead00")
            print("你输了")
            time.sleep(3)
            return
        if self.overdrivemode == True:
            print("\033[91m")
        else:
            print("\033[0m")
        if self.curyoukai["name"] == "Eduarte":
            if self.curyoukai["health"] <= 0:
                return
        if self.remainYoukais <= 0:
            self.randomChoice(self.boss)
        elif self.remainYoukais > 0:
            self.remainYoukais -= 1
                
        print("(这是水印)这是一个体验版本，不代表做完后的样子。")
        print("如果发现bug请反馈到邮箱 minqwq723897@outlook.com")
        print("版本 " + self.VERSION)
        print("\ndebugs: " + str(self.remainYoukais))
        print("当前妖怪名字: " + self.curyoukai["name"])
        print("防 " + str(self.curyoukai["defend"]) + ", 攻 " + str(self.curyoukai["attack"]) + ", 对方当前血量: " + str(self.curyoukai["health"]))
        print("分数 " + str(round(self.gamescore)) + ", 可再超载 " + str(self.overdrives) + " 次, 还有 " + str(self.spells) + " 个灵符")
        print("自身血量 " + str(self.playerhealth))
        print("1:攻击")
        print("2:bomb")
        print("3:我不玩了")
        print("4:超载机能")
        if self.gamedevmode:
            print("5:添加100个灵符")
            print("6:下一个")
            print("7:清空自身血量")
            print("8:startbossfight.name")
            print("9:返回菜单")
        choice = input("选择一个选项然后继续 >>> \033[0m").strip()
        if self.overdrivemode:
            print("\033[91m")
        if choice == "1":
            self.playSound("select00")
            for i, weapon in enumerate(self.weapons):
                print(str(i + 1) + 
                    ":" + 
                    weapon["name"] + 
                    "(" + 
                    (
                        str(weapon["damage"]) if isinstance(weapon["damage"], int) else (
                            str(weapon["damage"]["start"]) + 
                            " ~ " + 
                            str(weapon["damage"]["stop"])
                        )
                    ) + 
                    ")" + 
                    (
                        (
                            "(超载模式:" + 
                            (
                                (
                                    str(weapon["overdrive"]["start"]) + 
                                    " ~ " + 
                                    str(weapon["overdrive"]["stop"])
                                ) if isinstance(weapon["overdrive"], dict) else str(weapon["overdrive"])
                            ) + 
                            ")"
                        ) if weapon["overdrive"] != False else ""
                    )
                )
            try:
                choice = int(input("选择编号 >>> \033[0m").strip()) - 1
            except ValueError:
                print("输入错误")
                time.sleep(2)
            else:
                if self.overdrivemode:
                    print("\033[91m")
                self.playSound("ok00")
                if len(self.weapons) > choice:
                    weapon = self.weapons[choice]
                    if weapon["broken"] != False and random.randint(1, weapon["broken"]["stop"]) == 1:
                        print(weapon["broken"]["msg"])
                        time.sleep(1)
                    else:    
                        damage = weapon["damage"] if (weapon["overdrive"] != False and self.overdrivemode) != True else weapon["overdrive"]
                        if isinstance(damage, dict):
                            damage = random.randint(damage["start"], damage["stop"])
                        self.curyoukai["health"] -= damage
                        print("对方受到伤害 " + str(damage))
                        self.playSound("tan00")
                        time.sleep(1)
                        self.gamescore += random.randint(20000, 45000) * self.curyoukai["defend"] * damage / 50
                        self.playerhealth -= self.curyoukai["attack"]
        elif choice == "2": # 这个选项单独做出来不知道是什么意思
            self.playSound("ok00")
            if self.spells <= 0:
                print("灵符不足")
                time.sleep(1)
            else:
                print("奇迹「七彩大炮」！！")
                time.sleep(1)
                self.playSound("nep00")
                damage = random.randint(350, 700)
                self.curyoukai["health"] -= damage
                print("对方受到伤害 " + str(damage))
                time.sleep(1)
                self.gamescore += random.randint(20000, 45000) * self.curyoukai["defend"]
                self.spells -= 1
        elif choice == "3":
            sys.exit(0)
        elif choice == "4":
            if self.overdrives > 0 and self.overdrivemode == False:
                self.overdrives -= 1
                self.overdrivemode = True
                self.playSound("extend")
            else:
                print("不需要这样做")
                time.sleep(1)
        elif self.gamedevmode:
            if choice == "5":
                self.spells += 100
            elif choice == "6":
                self.randomChoice()
            elif choice == "7":
                self.playerhealth = 0
            elif choice == "8":
                self.randomChoice(self.boss)
            elif choice == "9":
                return # TODO: 恢复音乐
        if self.gamedevmode:
            input("按下Enter继续主循环")
        if initialgamescore != self.gamescore:
            self.saveRanking()
        self.mainLoop()
    def randomChoice(self, tiny_youkais = None):
        if tiny_youkais is None:
            tiny_youkais = self.tiny_youkais
        self.curyoukai = random.choice(tiny_youkais)
        if isinstance(self.curyoukai["defend"], dict):
            self.curyoukai["defend"] = round(random.uniform(self.curyoukai["defend"]["start"], self.curyoukai["defend"]["stop"]), 2)
        if isinstance(self.curyoukai["attack"], dict):
            self.curyoukai["attack"] = random.randint(self.curyoukai["attack"]["start"], self.curyoukai["attack"]["stop"])
        if isinstance(self.curyoukai["health"], dict):
            self.curyoukai["health"] = random.randint(self.curyoukai["health"]["start"], self.curyoukai["health"]["stop"])
    def saveRanking(self):
        # 只在游戏结束或章节完成时保存
        if self.playerhealth <= 0 or (self.curyoukai["name"] == "Eduarte" and self.curyoukai["health"] <= 0):
            yourName = ""
            nextChapterSel = ""
            while yourName == "":
                yourName = input("输入你的名字...\n> ")
                
            with open("score/ranking.txt", "a", encoding="utf-8") as f:
                f.write("\n================| " + time.asctime() + " |================\n")
                f.write("Chapter 1 | 分数 " + str(round(self.gamescore)) + " | 由 " + yourName + " 达成\n")
                
            while nextChapterSel == "":
                nextChapterSel = input("下一章(1)还是退出(2)？[1/2] ")
                if nextChapterSel == "1":
                    runSubProgram("chapter/002.py")
                    print("(这里暂停一秒是因为看不到报错)")
                    time.sleep(1)
                elif nextChapterSel == "2":
                    sys.exit()

Chapter1()
Chapter1.saveRanking()
pygame.mixer.music.stop() # 在完成章节后停掉音乐
