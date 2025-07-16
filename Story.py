from JsonTypes import *
from JsonReader import *
from Player import *
from constants import *
import time

from Utility import Question, Seperate


class StoryManager:
    def __init__(self, story_data):
        self.story_data = story_data
        self.current_node = "start"

    def run_node(self, player: Player) -> bool:
        Seperate()

        # Get Current Node
        if self.current_node in self.story_data["story_nodes"]:  # Check if the node exists in our json file
            node_data = self.story_data["story_nodes"][self.current_node] # Get the current node, now that we know it exists.
        else:
            # Not existing node => return to start
            raise NotImplementedError("Node: " + self.current_node + " not found")

        # Get the node as the StoryNode class from the JsonTypes file.
        node = StoryNode(node_data)

        # Show dialog
        dialog: str = node.dialog
        dialog = dialog.replace("YOUR_NAME", player.name)
        dialog = dialog.replace("YOUR_FRIEND_NAME", constants.FRIEND_NAME)
        print(dialog)
        time.sleep(2)

        # Check if the node is an ending
        if node.type == "ending":
            if node.outcome == "success":
                print("-----------------")
                print("Du hast gewonnen!")
                print("-----------------")
                pass
            else:
                print("-----------------")
                print("Du hast verloren!")
                print("-----------------")
                pass
            return False # Return false, to indicate, that the game is over.

        # Show choices

        # Get choices
        choices = []
        for choice in node.choices:
            text: str = choice["text"]
            text = text.replace("YOUR_NAME", player.name)
            text = text.replace("YOUR_FRIEND_NAME", constants.FRIEND_NAME)
            choices.append(text) # Append the choice text (description)

        # Ask question / Show choices
        answer = Question("Was möchtest du tun?", choices).Ask()

        # Check Answer
        choice = node.choices[answer - 1]
        # -1 because if the player picks answer 1 we want to get the first object in list which is at index 0

        if "requirements" in choice: # Check if there are requirements or not.
            for skill, value in choice["requirements"].items(): # Go throw all the requirements
                if not self.check_requirement(player, skill, value):
                    if not "failed" in choice:
                        print("Json didn't account for this. You didn't met the requirements to get here. But no fallback was defined. Define a callback in the json file by using the 'failed' key word.")
                        return False  # Return false, to indicate, that the game is over.
                    else:
                        failed_fallback = choice["failed"]
                        self.current_node = failed_fallback
                        return True

        self.current_node = choice["next"] # Set the next current node to be the next node, for continuing the game.
        return True

    def check_requirement(self, player: Player, skill: str, value: int) -> bool:
        # Check, if the player meets the requirements to pass this way or not.
        match skill:
            case "staerke":
                return player.strength >= value
            case "intelligenz":
                return player.intelligence >= value
            case "glück":
                return player.luck >= value
        return False

def RunStory(player: Player):
    # Lade JSON Daten
    story_data = Read_Json_File("decisionTree.json")

    # Create a story manager
    story: StoryManager = StoryManager(story_data)

    while True:
        inGame: bool = story.run_node(player)

        # if the .run_node returns false, the game has ended => inGame is false.
        # if the .run_node returns true, the game is still playing => inGame is true.

        if not inGame: # Check if the game is finished. If it is, break out of the while loop.
            break