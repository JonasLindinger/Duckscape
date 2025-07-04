from Utility import *

class D1:
    def __init__(self):
        pass

    def Start(self):

        # Create space between old and new question
        for i in range(2):
            print("")

        print("Start Question 1")

        print("--------------------")
        print("Erste Entscheidung")
        print("Du bist eine Ente im Zoo. Du willst ausbrechen.")
        print("")

        # Ask Question
        question_message: str = "Was willst du tun?"
        question_answers: list = ["Zaun inspizieren", "Teich beobachten"]
        question: Question = Question(question_message, question_answers)
        choice: int = question.Ask()

        # Redirect player to next question
        match choice:
            case 1:
                next: D2 = D2()
                next.Start()
            case 2:
                next: D3 = D3()
                next.Start()

class D2:
    def __init__(self):
        pass

    def Start(self):
        print("Start Question 2")

class D3:
    def __init__(self):
        pass

    def Start(self):
        # Create space between old and new question
        for i in range(2):
            print("")

        print("Start Question 3")

        print("--------------------")
        print("Tierpfleger naht")
        print("")

        # Ask Question
        question_message: str = "Was willst du tun?"
        question_answers: list = ["Schlafen stellen", "In Schatten schwimmen"]
        question: Question = Question(question_message, question_answers)
        choice: int = question.Ask()

        # Redirect player to next question
        match choice:
            case 1:
                pass
            case 2:
                pass