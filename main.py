from SkillPointSystem import *
from Dialogs import *
from Story import *

# Starting Dialog
ask_for_name: Dialog1_Ask_for_name = Dialog1_Ask_for_name()
ask_for_name.Run()

# Create Character and choose name
player: Player = Player(input("[Du] Ich heiße "))
time.sleep(2)

# Dialog 2
introduction_to_story: Dialog2_Introduction_to_story = Dialog2_Introduction_to_story(player)
introduction_to_story.Run()

# Dialog 3
ability_dialog: Dialog3_ability = Dialog3_ability(player)
ability_dialog.Run()

# Choose skills
skillPointSystem: SkillPointSystem = SkillPointSystem(player)
skillPointSystem.StartConfiguration()

# Run story from json
RunStory(player)