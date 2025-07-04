class Player:
    CONST_STARTING_POINTS_TO_SPEND = 21

    def __init__(self, name):
        self.name: str = name

        self.pointsToSpend: int = Player.CONST_STARTING_POINTS_TO_SPEND

        self.strength: int = 0      # Stärke
        self.speed: int = 0         # Geschwindigkeit
        self.skill: int = 0         # Geschick
        self.intelligence: int = 0  # Intelligenz

    def Print_Skill_Points(self):
        print("Strength: " + str(self.strength))
        print("Geschwindigkeit: " + str(self.speed))
        print("Geschick: " + str(self.skill))
        print("Intelligenz: " + str(self.intelligence))

    def Reset_Skill_Points(self):
        self.strength: int = 0
        self.speed: int = 0
        self.skill: int = 0
        self.intelligence: int = 0

        self.pointsToSpend: int = Player.CONST_STARTING_POINTS_TO_SPEND