from Utility import *
from constants import *
from Player import *

class D1:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        # Create space between old and new question
        for i in range(2):
            print("")

        print("--------------------")
        print("")

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
                next: D1_1_1 = D1_1_1(self.player)
            case 2:
                next: D1_2_1 = D1_2_1(self.player)
            case 3:
                next: D1_3_1 = D1_3_1(self.player)
            case 4:
                next: D1_4_1 = D1_4_1(self.player)

        if (next == None):
            raise RuntimeError("No valid decision was made.")

        next.Start()

# Naming: D = Decision. First digit = cheapter. Last digits = decision way.
# For example: D1_1_1 = Cheapter 1, first way, first decision.

# ----- Cheapter 1: The Cage -----

class D1_1_1:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        # Create space between old and new question
        for i in range(2):
            print("")

        print("--------------------")
        print("")

        # Todo: Add Dialog

        # Check if the player has the skill for this way.
        if (self.player.strength < 8 or self.player.speed < 10):
            # Player can't pass!
            # Todo: End the game here, because the player is stuck on the fence
            return

        next: D2 = D2(self.player)
        next.Start()

class D1_2_1:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        # Create space between old and new question
        for i in range(2):
            print("")

        print("--------------------")
        print("")

        # Todo: Add Dialog

        # Check if the player has the skill for this way.
        if (self.player.skill < 10 or self.player.strength > 4 or self.player.intelligence < 4):
            # Player can't pass!
            # Todo: End the game here, because the player is stuck in the fence
            return

        next: D2 = D2(self.player)
        next.Start()

class D1_3_1:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
        # Create space between old and new question
        for i in range(2):
            print("")

        # Todo: Add Dialog

        print("--------------------")
        print("")

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
         # Create space between old and new question
        for i in range(2):
            print("")

        # Todo: Add Dialog

        print("--------------------")
        print("")

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
         # Create space between old and new question
        for i in range(2):
            print("")

        # Todo: Add Dialog

        print("--------------------")
        print("")

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
         # Create space between old and new question
        for i in range(2):
            print("")

        # Todo: Add Dialog

        print("--------------------")
        print("")

        # Check if the player has the skill for this way.
        if (True):
            # Player can't pass!
            # End: Caught, because you were too loud and too weak. There is no way you are able to open a locked drawer.
            return


class D1_4_2_2:
    def __init__(self, player: Player):
        self.player: Player = player

    def Start(self):
         # Create space between old and new question
        for i in range(2):
            print("")

        # Todo: Add Dialog

        print("--------------------")
        print("")

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
        # Todo: Continue the story
        pass