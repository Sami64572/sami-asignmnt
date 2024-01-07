class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self, user):
        score = 0
        for question in self.questions:
            print(question.text)
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")

            user_answer = int(input("Your answer (enter the option number): "))
            if question.is_correct(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_option}\n")

        user.update_score(self.name, score)


class User:
    def __init__(self, username):
        self.username = username
        self.scores = {}

    def update_score(self, quiz_name, score):
        if quiz_name in self.scores:
            self.scores[quiz_name] += score
        else:
            self.scores[quiz_name] = score

    def display_scores(self):
        print(f"Scores for {self.username}:")
        for quiz, score in self.scores.items():
            print(f"{quiz}: {score}")


question1 = Question("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2)
question2 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2)
question3 = Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2)

quiz1 = Quiz("General Knowledge Quiz", [question1, question2, question3])

user1 = User("JohnDoe")

quiz1.take_quiz(user1)

user1.display_scores()