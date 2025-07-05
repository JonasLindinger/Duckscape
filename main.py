from SkillPointSystem import *
from Decision import *
from Dialogs import *
from Player import *
import time

# Run settings
isDebugRun: bool = True

FRIEND_NAME: str = "Joseph"

# Story
if not isDebugRun:
    ask_for_name: Dialog1_Ask_for_name = Dialog1_Ask_for_name()
    ask_for_name.Run()

# Create Character
if not isDebugRun:
    player: Player = Player(input("[Du] Ich heiße "))
    time.sleep(2)
else:
    player: Player = Player("Tester")

if not isDebugRun:
    introduction_to_story: Dialog2_Introduction_to_story = Dialog2_Introduction_to_story(player)
    introduction_to_story.Run()

if not isDebugRun:
    ability_dialog: Dialog3_ability = Dialog3_ability(player)
    ability_dialog.Run()

# Choose skills
skillPointSystem: SkillPointSystem = SkillPointSystem(player)
skillPointSystem.StartConfiguration()

# Start adventure
starting_decision: D1 = D1()
starting_decision.Start()