# THIS IS A DEMO VERSION AND NOT ARE THE RELEASE VERSION EXPRIENCE
# Flandre Studio 20250322
# Copyright (c) 2025 minqwq

import pygame
import os
import sys
import json
import random
import time

class Chapter1:
    VERSION = "Preview 0.02a"
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
        self.gamedir = os.path.dirname(os.path.abspath(__file__)) + os.sep
        self.gameconfig = json.load(open(self.gamedir + "config.json", "r", encoding="utf-8"))
        self.overdrives = int(self.gameconfig["overdrives"])
        self.spells = int(self.gameconfig["spells"]) # TODO: 修复类型错误
        self.gamedevmode = self.gameconfig["devmode"] == "true"
        if self.gamedevmode:
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
        if self.curyoukai["health"] <= 0: # FIXME: 有的时候血量变负值都没有触发死亡
            self.playSound("pldead00")
            self.playerhealth += self.curyoukai["health"] / 8 + 350;
            self.randomChoice()
        if self.playerhealth <= 0:
            self.playSound("pldead00")
            print("你输了")
            time.sleep(3)
            return
        if self.overdrivemode:
            print("\033[91m")
        else:
            print("\033[0m")
        print("(这是水印)这是一个体验版本，不代表做完后的样子。")
        print("版本 " + self.VERSION)
        print()
        print("当前妖怪名字: " + self.curyoukai["name"])
        print("防 " + str(self.curyoukai["defend"]) + ", 攻 " + str(self.curyoukai["attack"]) + ", 对方当前血量: " + str(self.curyoukai["health"]))
        print("分数 " + str(round(self.gamescore)) + ", 可再超载 " + str(self.overdrives) + " 次, 还有 " + str(self.spells) + " 个符卡")
        print("自身血量 " + str(self.playerhealth))
        print("1:攻击")
        print("2:bomb")
        print("3:我不玩了")
        print("4:超载机能")
        if self.gamedevmode:
            print("5:添加100个符卡")
            print("6:下一个对手")
            print("7:清空自身血量")
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
                choice = int(input("选择编号 >>> ").strip()) - 1
            except ValueError:
                print("输入错误")
                time.sleep(2)
            else:
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
                print("符卡不足")
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
            self.overdrives -= 1
            self.overdrivemode = True
            self.playSound("extend")
        elif self.gamedevmode:
            if choice == "5":
                self.spells += 100
            elif choice == "6":
                self.randomChoice()
            elif choice == "7":
                self.playerhealth = 0
        if self.gamedevmode:
            input("按下Enter继续主循环")
        self.mainLoop()
    def randomChoice(self):
        self.curyoukai = random.choice(self.tiny_youkais) # TODO: 随机防御值生命值
        if isinstance(self.curyoukai["attack"], dict):
            self.curyoukai["attack"] = random.randint(self.curyoukai["attack"]["start"], self.curyoukai["attack"]["stop"])
Chapter1()