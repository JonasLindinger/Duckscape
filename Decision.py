from Utility import *
from constants import *
from Player import *
import time


# ---- Decision 1: Initial Escape ----
def D1(player: Player):
    """Starting point of the story - First escape attempt"""
    Seperate()
    print("** Nacht im Zoo. Zeit für die Flucht! **")
    time.sleep(2)

    question_message: str = "Wie beginnst du deine Flucht?"
    question_answers: list = ["Durch den Wartungsbereich [Geschick]",
                              "Über den Zaun klettern [Stärke]",
                              "Den Wärter ablenken [Intelligenz]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 2: Maintenance Area ----
def D2(player: Player):
    """Maintenance area path"""
    question_message: str = "Du bist im Wartungsbereich. Was nun?"
    question_answers: list = ["Werkzeuge suchen [Intelligenz]",
                              "Durch Lüftung kriechen [Geschick]",
                              "Tür aufbrechen [Stärke]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 3: Storage Room ----
def D3(player: Player):
    """Storage room decisions"""
    question_message: str = "Der Lagerraum - welcher Weg?"
    question_answers: list = ["Kartons stapeln [Stärke]",
                              "Nach Schlüssel suchen [Intelligenz]",
                              "Durch Fenster [Geschick]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 4: Guard Post ----
def D4(player: Player):
    """Guard post encounter"""
    question_message: str = "Ein Wachposten! Was tust du?"
    question_answers: list = ["Verstecken [Geschick]",
                              "Geräusch erzeugen [Intelligenz]",
                              "Schnell vorbeirennen [Geschwindigkeit]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 5: Delivery Area ----
def D5(player: Player):
    """Delivery area choices"""
    question_message: str = "Der Lieferantenbereich - wie weiter?"
    question_answers: list = ["LKW untersuchen [Intelligenz]",
                              "Über Kisten klettern [Geschick]",
                              "Tor öffnen [Stärke]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 6: Vehicle Area ----
def D6(player: Player):
    """Vehicle area decisions"""
    question_message: str = "Zwischen den Fahrzeugen - was nun?"
    question_answers: list = ["In LKW verstecken [Geschick]",
                              "Fahrzeug kurzschließen [Intelligenz]",
                              "Zu Fuß weiter [Geschwindigkeit]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 7: Main Gate Area ----
def D7(player: Player):
    """Main gate area choices"""
    question_message: str = "Das Haupttor ist in Sicht!"
    question_answers: list = ["Pförtner ablenken [Intelligenz]",
                              "Über Zaun klettern [Stärke]",
                              "Durch Büsche schleichen [Geschick]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 8: Side Entrance ----
def D8(player: Player):
    """Side entrance options"""
    question_message: str = "Der Seiteneingang - wie durchkommen?"
    question_answers: list = ["Schloss knacken [Geschick]",
                              "Tür aufbrechen [Stärke]",
                              "Wachablösung abwarten [Intelligenz]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 9: Park Area ----
def D9(player: Player):
    """Park area choices"""
    question_message: str = "Im Parkbereich - welcher Weg?"
    question_answers: list = ["Durch Büsche [Geschick]",
                              "Über Parkplatz rennen [Geschwindigkeit]",
                              "Karte studieren [Intelligenz]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 10: Street Corner ----
def D10(player: Player):
    """Street corner decisions"""
    question_message: str = "An der Straßenecke - wie weiter?"
    question_answers: list = ["Bus nehmen [Intelligenz]",
                              "Durch Gassen [Geschick]",
                              "Direkte Route [Geschwindigkeit]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 11: City Area ----
def D11(player: Player):
    """City area options"""
    question_message: str = "In der Stadt - wohin?"
    question_answers: list = ["Zum Bahnhof [Intelligenz]",
                              "In den Park [Geschick]",
                              "Zur Bushaltestelle [Geschwindigkeit]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 12: Transport Hub ----
def D12(player: Player):
    """Transport hub choices"""
    question_message: str = "Am Verkehrsknotenpunkt - was nun?"
    question_answers: list = ["Zug nehmen [Intelligenz]",
                              "Taxi rufen [Geschick]",
                              "Zu Fuß weiter [Geschwindigkeit]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 13: Final Approach ----
def D13(player: Player):
    """Final approach decisions"""
    question_message: str = "Fast geschafft - letzte Entscheidung?"
    question_answers: list = ["Vorstadt [Geschick]",
                              "Waldgebiet [Stärke]",
                              "Hauptstraße [Geschwindigkeit]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 14: Last Obstacle ----
def D14(player: Player):
    """Last obstacle choices"""
    question_message: str = "Ein letztes Hindernis!"
    question_answers: list = ["Umgehen [Intelligenz]",
                              "Überwinden [Stärke]",
                              "Durchschlüpfen [Geschick]"]

    return Question(question_message, question_answers).Ask()


# ---- Decision 15: Final Choice ----
def D15(player: Player):
    """Final decision"""
    question_message: str = "Die finale Entscheidung!"
    question_answers: list = ["In die Berge [Stärke]",
                              "In die Stadt [Intelligenz]",
                              "Ans Meer [Geschick]"]

    return Question(question_message, question_answers).Ask()


# ---- Endings ----
def EndingSuccess(player: Player, type: str):
    """Successful escape endings"""
    Seperate()
    match type:
        case "mountains":
            print("=== ENDE: Freiheit in den Bergen ===")
        case "city":
            print("=== ENDE: Ein neues Leben in der Stadt ===")
        case "sea":
            print("=== ENDE: Abenteuer am Meer ===")
    time.sleep(2)

def EndingCaught(player: Player):
    """Getting caught ending"""
    Seperate()
    print("=== ENDE: Zurück in den Zoo ===")
    time.sleep(2)

def CheckSkill(player: Player, choice: int) -> bool:
    """Helper function to check if player has required skills"""
    required_skill = 5  # Base requirement
    match choice:
        case 1:
            return player.skill >= required_skill
        case 2:
            return player.strength >= required_skill
        case 3:
            return player.intelligence >= required_skill
    return False