class Question:
    def __init__(self, question: str, answers: list):
        self.question_text: str = question
        self.answers: list = answers

    def Ask(self) -> int:

        # Ask Question
        print(self.question_text)

        i: int = 0
        for answer in self.answers:
            print(str(i + 1) + ". " + answer)
            i += 1

        # Wait for a valid answer
        while True:
            # Collect the user input
            given_answer: str = input("Deine Entscheidung: ")

            # Remove spaces and dots for a better user experience
            given_answer: str = given_answer.replace(" ", "")
            given_answer: str = given_answer.replace(".", "")

            try:
                # Hope, that the user input was a number, that's why I use a try here.
                answer_index: int = int(given_answer)

                # Check if the answer is valid
                if (answer_index > len(self.answers) or answer_index <= 0):
                    print("Antwort muss zwischen 1 und " + str(len(self.answers)) + " sein!")
                    continue

                return answer_index
            except ValueError:
                print("Bitte gib eine Zahl ein!")
                continue