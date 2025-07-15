from Player import *
from Utility import *


class SkillPointSystem:
    def __init__(self, player: Player):
        self.player: Player = player

    def StartConfiguration(self):
        # Strength
        self.AskStrength()

        # Intelligence
        self.AskIntelligence()

        # Skill
        self.AskLuck()

        # Ask if everything is fine or if changes should be made.
        while True:
            print("")
            self.player.Print_Skill_Points()
            print("")
            question_message: str = "Bist du zufrieden mit deiner Punkte verteilung? Du hast noch " + str(self.player.pointsToSpend) + " Punkte übrig."
            question_answers: list = [
                "Ich bin zufrieden.",
                "Ich möchte alles neu machen.",
                "Ich möchte meine Stärke ändern.",
                "Ich möchte mein Intelligenz ändern."
                "Ich möchte mein Glück ändern.",
            ]
            question: Question = Question(question_message, question_answers)
            answer: int = question.Ask()

            match answer:
                case 1: # Player is satisfied with the configuration
                    break
                case 2: # We start a new SkillPointSystem which should refall back here and continue perfectly fine.
                    self.player.Reset_Skill_Points()

                    new_point_system: SkillPointSystem = SkillPointSystem(self.player)
                    new_point_system.StartConfiguration()
                    break
                case 3: # Ask strength
                    self.AskStrength()
                case 4: # Ask Intelligence
                    self.AskIntelligence()
                case 5: # Ask luck
                    self.AskLuck()

    def AskStrength(self):
        # Strength
        question_min_included: int = 0
        question_max_included: int = -1
        question_message: str = ""
        if self.player.strength > 0:
            question_message: str = "Setzte die Punkte für Stärke(" + str(self.player.strength) + ")  (" + str(self.player.pointsToSpend) + " Punkte Übrig.)"
            question_max_included = self.player.strength
        else:
            question_message: str = "Setzte die Punkte für Stärke (" + str(self.player.pointsToSpend) + " Punkte Übrig.)"
            question_max_included = min(self.player.pointsToSpend, 10)

        skill_question: Skill_Question = Skill_Question(question_message, question_min_included,
                                                        question_max_included)
        strength: int = skill_question.Ask()

        # Subtract or Add points depending on the previous value.
        additiveNumber: int = self.player.strength - strength
        self.player.pointsToSpend += additiveNumber

        # Set the new value
        self.player.strength = strength

    def AskIntelligence(self):
        # Intelligence
        question_min_included: int = 0
        question_max_included: int = -1
        question_message: str = ""
        if self.player.intelligence > 0:
            question_message: str = "Setzte die Punkte für Intelligenz(" + str(self.player.intelligence) + ")  (" + str(self.player.pointsToSpend) + " Punkte Übrig.)"
            question_max_included = self.player.intelligence
        else:
            question_message: str = "Setzte die Punkte für Intelligenz (" + str(self.player.pointsToSpend) + " Punkte Übrig.)"
            question_max_included = min(self.player.pointsToSpend, 10)
        skill_question: Skill_Question = Skill_Question(question_message, question_min_included, question_max_included)
        intelligence: int = skill_question.Ask()

        # Subtract or Add points depending on the previous value.
        additiveNumber: int = self.player.intelligence - intelligence
        self.player.pointsToSpend += additiveNumber

        # Set the new value
        self.player.intelligence = intelligence

    def AskLuck(self):
        # Speed
        question_min_included: int = 0
        question_max_included: int = -1
        question_message: str = ""
        if self.player.luck > 0:
            question_message: str = "Setzte die Punkte für Glück(" + str(self.player.luck) + ")  (" + str(self.player.pointsToSpend) + " Punkte Übrig.)"
            question_max_included = self.player.luck
        else:
            question_message: str = "Setzte die Punkte für Glück (" + str(self.player.pointsToSpend) + " Punkte Übrig.)"
            question_max_included = min(self.player.pointsToSpend, 10)
        skill_question: Skill_Question = Skill_Question(question_message, question_min_included, question_max_included)
        luck: int = skill_question.Ask()

        # Subtract or Add points depending on the previous value.
        additiveNumber: int = self.player.luck - luck
        self.player.pointsToSpend += additiveNumber

        # Set the new value
        self.player.luck = luck