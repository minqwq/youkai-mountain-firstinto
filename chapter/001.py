# THIS IS A DEMO VERSION AND NOT ARE THE RELEASE VERSION EXPRIENCE
# Flandre Studio 20250322
# Everything by minqwq

import pygame
import os
import sys
import json
import random
import time
import base64

# 防御的计算方式是 "<受伤值> / <防御>"
# 137 / 1.5 = 91.333333

pygame.mixer.init()
pygame.mixer.music.load("music/gf01_02.mp3")
pygame.mixer.music.play()

sfx_select00 = pygame.mixer.Sound("sfx/select00.wav")
sfx_nep00 = pygame.mixer.Sound("sfx/nep00.wav")
sfx_ok00 = pygame.mixer.Sound("sfx/ok00.wav")
sfx_extend = pygame.mixer.Sound("sfx/extend.wav")
sfx_tan00 = pygame.mixer.Sound("sfx/tan00.wav")
sfx_pldead00 = pygame.mixer.Sound("sfx/pldead00.wav")

configFile = open("config.json", "r", encoding="utf-8")
configRead = json.load(configFile)
overdrive_remain = int(configRead["overdrives"])

score = 0
overdrive_mode = 0
spellremain = int(configRead["spells"])
yk_health = 0
version = "Preview 0.02a"
oldknifeisok = True
devmode = configRead["devmode"]
devmodepwd = base64.b64decode(b'bGlmZWlzdG91aG91') # lifeistouhou
seledatk = False
local_health = 3500

def resetconf():
    if overdrive_remain > 6:
        print("config incorrect(> 6)")
        sys.exit()
    if spellremain > 6:
        print("config incorrect(> 6)")
        sys.exit()

if devmode == "false":
    resetconf()

if devmode == "true":
    devmodepwdinput = input("输入开发模式密码 > ")
    if bytes(devmodepwdinput, encoding="utf-8") == devmodepwd:
        spellremain = 9999
        overdrive_remain = 9999
    else:
        resetconf()

tiny_youkais = [
                   "大妖精",
                   "琪露诺",
                   "幽灵",
                   "不保存姐",
                   "小女仆",
                   "小妖精"
               ]
              
sel0 = ['''
def attacking():
    print("选一个物品吧")
    print(
            "1:生锈到快断掉的刀(50 ~ 160)"+
            "\n2:锤ta(70 ~ 100)(Overdrive mode:150 ~ 270)"+
            "\n3:脚踢(80 ~ 130)(Overdrive mode:200 ~ 350)"
         )
    selatkitem = input("选择编号 >>> ")
    if selatkitem == "1":
        if oldknifeisok == False:
            oldknifebrokentry = random.randint(1, 20)
            if oldknifebrokentry == "1":
                print("刀断了...")
                oldknifeisok = False
                time.sleep(1)
            else:
                stdatk = random.randint(50, 160)
                yk_health -= stdatk
                print("对方受到伤害 " + stdatk)
                sfx_tan00.play()
                time.sleep(1)
        else:
            print("断了，不能用刀把。")
            time.sleep(1)
    elif selatkitem == "2":
        if overdrive_mode >= 1:
            stdatk = random.randint(150, 270)
            yk_health -= stdatk
            print("对方受到伤害 " + stdatk)
            sfx_tan00.play()
            time.sleep(1)
        else:
            stdatk = random.randint(70, 100)
            yk_health -= stdatk
            print("对方受到伤害 " + stdatk)
            sfx_tan00.play()
            time.sleep(1)
    elif selatkitem == "3":
        if overdrive_mode >= 1:
            stdatk = random.randint(200, 350)
            yk_health -= stdatk
            print("对方受到伤害 " + stdatk)
            sfx_tan00.play()
            time.sleep(1)
        else:
            stdatk = random.randint(80, 130)
            yk_health -= stdatk
            print("对方受到伤害 " + stdatk)
            sfx_tan00.play()
            time.sleep(1)
''']

randomchoice = '''spellatklo = 350
spellatkhi = 700

curyoukainame = random.choice(tiny_youkais)
if curyoukainame == "大妖精":
    yk_defend = 1.2
    yk_attack = random.randint(80, 120)
    yk_health = 2000
elif curyoukainame == "琪露诺":
    yk_defend = 1.09
    yk_attack = random.randint(9, 99)
    yk_health = 1999
elif curyoukainame == "幽灵":
    yk_defend = 2
    yk_attack = random.randint(1, 50)
    yk_health = 1000
elif curyoukainame == "不保存姐":
    yk_defend = 1
    yk_attack = 1
    yk_health = 1
elif curyoukainame == "小女仆":
    yk_defend = 1.4
    yk_attack = random.randint(40, 130)
    yk_health = 1500
elif curyoukainame == "小妖精":
    yk_defend = 1.1
    yk_attack = random.randint(40, 60)
    yk_health = 1000'''
exec(randomchoice)    

while True:
    if overdrive_mode >= 1:
        print("\033[31m")
    elif overdrive_mode <= 0:
        print("\033[0m")
    if yk_health <= 0:
        sfx_pldead00.play()
        local_health += yk_health / 8 + 350
        exec(randomchoice)  
    clearScreen()
    print("(这是水印)这是一个体验版本，不代表做完后的样子。\n版本 " + version + "\n")
    print("当前妖怪名字: " + curyoukainame)
    print("防 " + str(yk_defend) + ", 攻 " + str(yk_attack) + ", 对方当前血量: " + str(yk_health))
    print("分数 " + str(round(score)) + ", 可再超载 " + str(overdrive_remain) + " 次, 还有 " + str(spellremain) + " 个符卡")
    print("自身血量 " + str(local_health))
    if overdrive_mode >= 1:
        print("超载模式还能再维持 " + str(overdrive_mode) + " 回")
    ykatk = input("1:攻击\n2:bomb\n3:我不玩了\n4:超载机能\n选择一个选项然后继续 >>> ")
    if ykatk == "1":
        sfx_select00.play()
        print("选一个物品吧")
        print(
                "1:生锈到快断掉的刀(50 ~ 160)"+
                "\n2:锤ta(70 ~ 100)(Overdrive mode:150 ~ 270)"+
                "\n3:脚踢(80 ~ 130)(Overdrive mode:200 ~ 350)"
             )
        selatkitem = input("选择编号 >>> ")
        if selatkitem == "1":
            sfx_ok00.play()
            oldknifebrokentry = random.randint(1, 20)
            if oldknifebrokentry == "1":
                print("刀断了...")
                oldknifeisok = False
                time.sleep(1)
            else:
                stdatk = random.randint(50, 160)
                yk_health -= stdatk
                print("对方受到伤害 " + str(stdatk))
                sfx_tan00.play()
                time.sleep(1)
                seledatk = True
        elif selatkitem == "2":
            sfx_ok00.play()
            if overdrive_mode > 0:
                stdatk = random.randint(150, 270)
                yk_health -= stdatk
                print("对方受到伤害 " + str(stdatk))
                sfx_tan00.play()
                time.sleep(1)
                overdrive_mode -= 1
                seledatk = True
            else:
                stdatk = random.randint(70, 100)
                yk_health -= stdatk
                print("对方受到伤害 " + str(stdatk))
                sfx_tan00.play()
                time.sleep(1)
                seledatk = True
        elif selatkitem == "3":
            sfx_ok00.play()
            if overdrive_mode > 0:
                stdatk = random.randint(200, 350)
                yk_health -= stdatk
                print("对方受到伤害 " + str(stdatk))
                sfx_tan00.play()
                overdrive_mode -= 1
                time.sleep(1)
                seledatk = True
            else:
                stdatk = random.randint(80, 130)
                yk_health -= stdatk
                print("对方受到伤害 " + str(stdatk))
                sfx_tan00.play()
                time.sleep(1)
                seledatk = True
        else:
            pass
        if seledatk == True:
            score += random.randint(20000, 45000) * yk_defend * stdatk / 50
            local_health -= yk_attack
            seledatk = False
        elif seledatk == False:
            pass
    elif ykatk == "2":
        sfx_ok00.play()
        if spellremain <= 0:
            print("符卡不足")
            time.sleep(1)
            continue
        print("奇迹「七彩大炮」！！")
        time.sleep(1)
        sfx_nep00.play()
        spellatk = random.randint(spellatklo, spellatkhi)
        yk_health -= spellatk
        print("对方受到伤害 " + str(spellatk))
        time.sleep(1)
        score += random.randint(20000, 45000) * yk_defend
        spellremain -= 1
    elif ykatk == "3":
        sys.exit()
    elif ykatk == "4":
        if overdrive_remain >= 0 and overdrive_mode <= 0:
            overdrive_mode = 5
            overdrive_remain -= 1
            print("已启用超载模式。")
            sfx_extend.play()
            time.sleep(1)
        else:
            print("没用。(可用为0或仍处于超载模式中)")
            time.sleep(1)
