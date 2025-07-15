class Player:
    CONST_STARTING_POINTS_TO_SPEND = 16

    def __init__(self, name):
        self.name: str = name

        self.pointsToSpend: int = Player.CONST_STARTING_POINTS_TO_SPEND

        self.strength: int = 0      # Stärke
        self.intelligence: int = 0  # Intelligenz
        self.luck: int = 0          # Glück

    def Print_Skill_Points(self):
        print("Strength: " + str(self.strength))
        print("Intelligenz: " + str(self.intelligence))
        print("Glück: " + str(self.luck))

    def Reset_Skill_Points(self):
        self.strength: int = 0
        self.intelligence: int = 0
        self.luck: int = 0

        self.pointsToSpend: int = Player.CONST_STARTING_POINTS_TO_SPEND