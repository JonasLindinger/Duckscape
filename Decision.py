from Utility import *
from constants import *
from Player import *
import random

class D1:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        Seperate()

        # Ask Question
        question_message: str = "Wie willst du und " + constants.FRIEND_NAME + " aus deinem Gehege kommen?"
        question_answers: list =    ["Fliege über den Zaun", 
                                    "Schleiche unter dem Zaun hindurch.",
                                    "Öffne das Tor, indem du und " + constants.FRIEND_NAME + "vorsichtig dagegen drückt.",
                                    "Frage " + constants.FRIEND_NAME + " nach einem Plan."]
        question: Question = Question(question_message, question_answers)
        choice: int = question.Ask()

        # Redirect player to next question

        next = None
        match choice:
            case 1:
                next: D1_1 = D1_1(self.player)
            case 2:
                next: D1_2 = D1_2(self.player)
            case 3:
                next: D1_3 = D1_3(self.player)
            case 4:
                next: D1_4_1 = D1_4_1(self.player)

        if (next == None):
            raise RuntimeError("No valid decision was made.")

        next.Start()

# Naming: D = Decision. First digit = cheapter. Last digits = decision way.
# For example: D1_1_1 = Cheapter 1, first way, first decision.

# ----- Cheapter 1: The Cage -----

class D1_1:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        Seperate()

        # Todo: Add Dialog

        # Check if the player has the skill for this way.
        if (self.player.strength < 8 or self.player.speed < 10):
            # Player can't pass!
            # Todo: End the game here, because the player is stuck on the fence
            return

        next: D2 = D2(self.player)
        next.Start()

class D1_2:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        Seperate()

        # Todo: Add Dialog

        # Check if the player has the skill for this way.
        if (self.player.skill < 10 or self.player.strength > 4 or self.player.intelligence < 4):
            # Player can't pass!
            # Todo: End the game here, because the player is stuck in the fence
            return

        next: D2 = D2(self.player)
        next.Start()

class D1_3:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        Seperate()

        # Check if the player has the skill for this way.
        if (self.player.strength < 10 or self.player.skill < 10):
            # Player can't pass!
            # Todo: End the game here, because the player was caught by a guard.
            return

        next: D2 = D2(self.player)
        next.Start()

class D1_4_1:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        Seperate()

        # Check if the player has the skill for this way.
        if (False):
            # Player can't pass!
            return

        next: D1_4_2 = D1_4_2(self.player)
        next.Start()

class D1_4_2:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        Seperate()

        # Check if the player has the skill for this way.
        if (False):
            # Player can't pass!
            return

        # Ask Question
        question_message: str = "Wo sucht ihr den Schlüssel?"
        question_answers: list =    ["Ihr sucht in der Schublade (Sie ist abgeschlossen und ihr musst sie aufbrechen!).", 
                                    "Ihr sucht auf dem Schreibtisch unten den tausenden Papierbergen.",
                                    "Gehe zurück."]
        question: Question = Question(question_message, question_answers)
        choice: int = question.Ask()

        # Redirect player to next question

        next = None
        match choice:
            case 1:
                next: D1_4_2_1 = D1_4_2_1(self.player)
            case 2:
                next: D1_4_2_2 = D1_4_2_2(self.player)
            case 3:
                next: D1 = D1(self.player)

        if (next == None):
            raise RuntimeError("No valid decision was made.")

        next.Start()

class D1_4_2_1:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        Seperate()

        # Check if the player has the skill for this way.
        if (True):
            # Player can't pass!
            # End: Caught, because you were too loud and too weak. There is no way you are able to open a locked drawer.
            return


class D1_4_2_2:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        Seperate()

        next = None
        # Check if the player has the skill for this way.
        if (self.player.skill < 8 or self.player.intelligence < 10):
            # Player can't pass!
            # End: You couldn't find the key and have to do another decision!
            next: D1_4_2 = D1_4_2(self.player)
            next.Start()
            return

        # Todo: Add Dialog (you use the key to open the door.)

        next: D2 = D2(self.player)
        next.Start()

# ----- Cheapter 2: The Zoo -----

class D2:
    def __init__(self, player: Player) -> None:
        self.player: Player = player

    def Start(self):
        Seperate()

        # Ask Question
        question_message: str = "Wie willst du aus dem Zoo entkommen?"
        question_answers: list = ["In einem Auto verstecken.",
                                  "Werter suchen.",
                                  "Kind suchen."]
        question: Question = Question(question_message, question_answers)
        choice: int = question.Ask()

        next = None
        match choice:
            case 1:
                next: D2_1_1 = D2_1_1(self.player)
            case 2:
                next: D2_2 = D2_2(self.player)
            case 3:
                next: D2_3 = D2_3(self.player)

        if (next == None):
            raise RuntimeError("No valid decision was made.")

        next.Start()

class D2_1_1:
    def __init__(self, player: Player) -> None:
        self.player: Player = player

    def Start(self):
        Seperate()

        # Todo: DO story stuff

class D2_2:
    def __init__(self, player: Player) -> None:
        self.player: Player = player

    def Start(self):
        Seperate()

        # Todo: DO story stuff

class D2_3:
    def __init__(self, player: Player) -> None:
        self.player: Player = player

    def Start(self):
        Seperate()

        # Generate a random number between 0 and 1
        roll = random.random()

        # If the number is less than 0.1 (10%) => pass
        # Otherwise (90% of the time), => not pass
        successful: bool = roll < 0.1

        if not successful:
            # Player can't pass!
            # End: You were caught by the parents, and they brought you back to the zoo.
            return

        # Todo: Add Dialog

        # End: Kid let you be free