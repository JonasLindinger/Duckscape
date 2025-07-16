from SkillPointSystem import *
from Dialogs import *
from Story import *

# Run settings
isDebugRun: bool = True

# Starting Dialog
if not isDebugRun:
    ask_for_name: Dialog1_Ask_for_name = Dialog1_Ask_for_name()
    ask_for_name.Run()

# Create Character and choose name
if not isDebugRun:
    player: Player = Player(input("[Du] Ich heiße "))
    time.sleep(2)
else:
    player: Player = Player("Tester")

# Dialog 2
if not isDebugRun:
    introduction_to_story: Dialog2_Introduction_to_story = Dialog2_Introduction_to_story(player)
    introduction_to_story.Run()

# Dialog 3
if not isDebugRun:
    ability_dialog: Dialog3_ability = Dialog3_ability(player)
    ability_dialog.Run()

# Choose skills
if not isDebugRun:
    skillPointSystem: SkillPointSystem = SkillPointSystem(player)
    skillPointSystem.StartConfiguration()
else:
    player.pointsToSpend = 0
    player.strength = 10
    player.speed = 10
    player.skill = 10
    player.intelligence = 10

# Run story from json
RunStory(player)