from Decision import *
from Dialogs import *
from Player import *

# Story
ask_for_name: Dialog1_Ask_for_name = Dialog1_Ask_for_name()
ask_for_name.Run()

# Create Character
player: Player = Player(input("[Du] Ich heiße "))
time.sleep(2)

introduction_to_story: Dialog2_Introduction_to_story = Dialog2_Introduction_to_story(player)
introduction_to_story.Run()

ability_dialog: Dialog3_ability = Dialog3_ability(player)
ability_dialog.Run()

# Start adventure
starting_decision: D1 = D1()
starting_decision.Start()