﻿import time
from Player import *
from main import *

class Dialog1_Ask_for_name:
    def __init__(self):
        pass
    def Run(self):
        print("[Fremde Ente] Heeee… dich hab ich hier noch nie gesehen.")
        time.sleep(3)
        print("[Fremde Ente] Bist du... neu?")
        time.sleep(2)
        print("** Du watschelst etwas verlegen. **")
        time.sleep(3)
        print("[Du] Vielleicht.")
        time.sleep(2)
        print("[Fremde Ente] Du siehst nicht aus wie eine Standard-Zoo-Ente. Kein Glanz im Gefieder, kein Interesse an Besucherkindern...")
        time.sleep(4)
        print("** Die Ente kommt näher, mustert dich. **")
        time.sleep(3)
        print("[Fremde Ente] Ich heiße " + str(FRIEND_NAME) + " und du?")
        time.sleep(1)

class Dialog2_Introduction_to_story:
    def __init__(self, player: Player):
        self.player: Player = player
    def Run(self):
        print("** Die Ente nickt langsam. **")
        time.sleep(2)
        print("[" + str(FRIEND_NAME) + "] Hmmm. " + self.player.name + " also. Klingt nicht nach einer Zoo-Ente. Klingt eher nach… einer Flucht.")
        time.sleep(4)
        print("** Kurze Pause. Die Ente blinzelt verschwörerisch. **")
        time.sleep(3)
        print("[" + str(FRIEND_NAME) + "] Wenn du hier raus willst – und ja, ich seh’s dir an – dann brauchst du mehr als hübsches Gefieder.")
        time.sleep(4)
        print("[" + str(FRIEND_NAME) + "] Lass uns zusammen ausbrechen!")
        time.sleep(2)
        print("[" + str(FRIEND_NAME) + "] Aber bevor wir genaueres planen, lass uns erstmal kennen lernen.")
        time.sleep(2)

class Dialog3_ability:
    def __init__(self, player: Player):
        self.player: Player = player

    def Run(self):
        print("[" + str(FRIEND_NAME) + "] Wie würdest du dich beschreiben?")
        time.sleep(3)
        print("[" + str(FRIEND_NAME) + "] Also stell` dir vor, du hast 21 Punkte und die verteilst du jetzt auf Stärke, Intelligenz und Geschick. Dabei kann jede Eigenschaft maximal 10 Punkte haben.")
        time.sleep(4)
        print("[" + str(FRIEND_NAME) + "] Zum Beispiel würde ich mich so beschreiben:")
        time.sleep(3)
        print("[" + str(FRIEND_NAME) + "] Stärke: 7")
        time.sleep(1)
        print("[" + str(FRIEND_NAME) + "] Geschwindigkeit: 6")
        time.sleep(1)
        print("[" + str(FRIEND_NAME) + "] Geschick: 4")
        time.sleep(1)
        print("[" + str(FRIEND_NAME) + "] Intelligenz: 4")
        time.sleep(3)
        print("[" + str(FRIEND_NAME) + "] Verstanden? 7 + 6 + 4 + 4 = 21")
        time.sleep(3)
        print("[" + str(FRIEND_NAME) + "] Jetzt bist du dran!")
