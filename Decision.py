from Utility import *
from constants import *
from Player import *
import random

def D1(player: Player):
    Seperate()

    # Ask Question
    question_message: str = "Wie willst du und " + constants.FRIEND_NAME + " aus deinem Gehege kommen?"
    question_answers: list = ["Fliege über den Zaun",
                              "Schleiche unter dem Zaun hindurch.",
                              "Öffne das Tor, indem du und " + constants.FRIEND_NAME + "vorsichtig dagegen drückt.",
                              "Frage " + constants.FRIEND_NAME + " nach einem Plan."]
    question: Question = Question(question_message, question_answers)
    choice: int = question.Ask()

    # Redirect player to next question

    match choice:
        case 1:
            D1_1(player)
        case 2:
            D1_2(player)
        case 3:
            D1_3(player)
        case 4:
            D1_4_1(player)

# Naming: D = Decision. First digit = cheapter. Last digits = decision way.
# For example: D1_1_1 = Cheapter 1, first way, first decision.

# ----- Cheapter 1: The Cage -----

def D1_1(player: Player):
    Seperate()
    # Todo: Add Dialog
    # Check if the player has the skill for this way.
    if (player.strength < 8 or player.speed < 10):
        # Player can't pass!
        # Todo: End the game here, because the player is stuck on the fence
        return
    D2(player)

def D1_2(player: Player):
    Seperate()
    # Todo: Add Dialog
    # Check if the player has the skill for this way.
    if (player.skill < 10 or player.strength > 4 or player.intelligence < 4):
        # Player can't pass!
        # Todo: End the game here, because the player is stuck in the fence
        return
    D2(player)

def D1_3(player: Player):
    Seperate()
    # Check if the player has the skill for this way.
    if (player.strength < 10 or player.skill < 10):
        # Player can't pass!
        # Todo: End the game here, because the player was caught by a guard.
        return
    D2(player)

def D1_4_1(player: Player):
    Seperate()
    # Check if the player has the skill for this way.
    if (False):
        # Player can't pass!
        return
    D1_4_2(player)

def D1_4_2(player: Player):
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
    match choice:
        case 1:
            D1_4_2_1(player)
        case 2:
            D1_4_2_2(player)
        case 3:
            D1(player)

def D1_4_2_1(player: Player):
    Seperate()
    # Check if the player has the skill for this way.
    if (True):
        # Player can't pass!
        # End: Caught, because you were too loud and too weak. There is no way you are able to open a locked drawer.
        return


def D1_4_2_2(player: Player):
    Seperate()
    # Check if the player has the skill for this way.
    if (player.skill < 8 or player.intelligence < 10):
        # Player can't pass!
        # End: You couldn't find the key and have to do another decision!
        D1_4_2(player)
        return

    # Todo: Add Dialog (you use the key to open the door.)

# ----- Cheapter 2: The Zoo -----

def D2(player: Player):
    Seperate()
    # Ask Question
    question_message: str = "Wie willst du aus dem Zoo entkommen?"
    question_answers: list = ["In einem Auto verstecken.",
                              "Werter suchen.",
                              "Kind suchen."]
    question: Question = Question(question_message, question_answers)
    choice: int = question.Ask()
    match choice:
        case 1:
            D2_1(player)
        case 2:
            D2_2(player)
        case 3:
            D2_3(player)

def D2_1(player: Player):
    Seperate()

    # Todo: DO story stuff

def D2_2(player: Player):
    Seperate()

    # Todo: DO story stuff

def D2_3(player: Player):
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