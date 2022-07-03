from time import sleep
import random
import sys
import os


correct_answer = None
received_question = None
scores = ["10", "20", "30", "40", "50"]
player = None
current_path = os.path.dirname(__file__)
questions_path = os.path.join(current_path, 'questions.csv')

def main():
    introduction()
    menu()

class Game:
    def __init__(self):
        self.difficulty = 0

    def raise_difficulty(self):
        self.difficulty += 1

    def intro_question(self):
        os.system("clear")
        print("")
        points = scores[self.difficulty]
        print("-" * 50)
        print(f"We are in the round {self.difficulty + 1} for {points} points.".center(50))
        print("If you wish to leave, you can answer 'exit'.".center(50))
        print("-" * 50)
        print("")

    def ask_question(self):
        global received_question, correct_answer

        questions = open(questions_path).read().splitlines()
        if self.difficulty == 0:
            randomquestion = random.choice(questions[:5])
        elif self.difficulty == 1:
            randomquestion = random.choice(questions[5:10])
        elif self.difficulty == 2:
            randomquestion = random.choice(questions[10:15])
        elif self.difficulty == 3:
            randomquestion = random.choice(questions[15:20])
        else:
            randomquestion = random.choice(questions[20:25])
        received_question = randomquestion.split(",")
        print(received_question[1])
        print(f"\n A. {received_question[2]}\t\t B. {received_question[3]}")
        print(f"\n C. {received_question[4]}\t\t D. {received_question[5]}")

        correct_answer = received_question[6]
        return correct_answer


    def validate_answer(self):
        global correct_answer, received_question

        acepted_answers = ["a", "b", "c", "d", "exit"]
        answer = input("\nYour answer: ").lower()

        if not (answer in acepted_answers):
            print("\n Please enter a valid answer. You can use 'exit' to leave the game.")
            self.validate_answer()
        elif (answer == 'exit'):
            sleep(1)
            if self.difficulty == 0:
                print (f"\n You have chosen to end the game, {player}. You have won 0 points. See you in the future!")
            else:
                print (f"\n You have chosen to end the game, {player}. You have won {scores[self.difficulty - 1]} points. Congratulations!")
                save_score(self.difficulty)
            sleep(3)
            os.system("clear")
            menu()
        elif (answer == "a" or answer == "b" or answer == "c" or answer == "d"):
            if (correct_answer == received_question[ord(answer)-95]):
                if (self.difficulty == 4):
                    os.system("clear")
                    sleep(1)
                    print(f"\n\t  ******* CONGRATULATIONS, {player.upper()}! *************\n")
                    sleep(0.7)
                    print("    ********* YOU HAVE ACHIEVED 50 POINTS! *************\n")
                    sleep(0.7)
                    print(" ¡You have reached the top, it was an excellent game! once again,\n")
                    print("\t********** CONGRATULATIONS!! *************\n")
                    print("\t *incredibly loud applause and cheers*\n")
                    save_score(self.difficulty + 1)
                    sleep(2)
                    menu()
                else:
                    sleep(2)
                    print("\n")
                    print(f"You have guessed right, {player}! Now you have {scores[self.difficulty]} points.".center(50))
                    print("\n\n")
                    print(f"Let's go to the round #{self.difficulty + 2}!".center(50))
                    sleep(3)
                    self.raise_difficulty()
                    self.intro_question()
                    self.ask_question()
                    self.validate_answer()

            else:
                sleep(2)
                print(f"\n Ops. The answer you have chosen is incorrect.\n\n The correct answer was: {correct_answer}.")
                sleep(3)
                print(f"\n your total score was {scores[self.difficulty - 1]} points.")
                print("\n\n Thanks for playing!")
                save_score(self.difficulty)

                volver_jugar = input("\n\n Would you like to try again? (y/n):  ")
                if (volver_jugar.lower() == "y"):
                    sleep(2)
                    new_game = Game()
                    new_game.intro_question()
                    new_game.ask_question()
                    new_game.validate_answer()
                else:
                    menu()

def save_score(score):
    file = open(os.path.join(current_path, "scores.txt"), "a")
    file.write(f"User: {player}.\t\t Score: {scores[score - 1]}.\n")
    file.close()

def load_scores():
    file = open(os.path.join(current_path, "scores.txt"))
    sleep(2)
    print("")
    print (file.read())
    file.close()

def introduction():
    print("\n\nLadies and Gentlemen!\n")
    sleep(1)
    print("Welcome to a new program of the QUESTIONS AND ANSWERS contest.\n")
    sleep(1)
    print("*applause*\n")
    sleep(1)
    print("OUR FIRST CONTESTANT IS...\n")
    sleep(1)
    print("...ehm...\n")
    sleep(1)
    global player
    player = input("Sorry, i forget your name. ¿What's your name? (write your name): ")
    print(" ")
    print("of course, that's your name!\n")
    sleep(1)
    print(f"Everyone, A BIG APPLAUSE FOR OUR CANDIDATE {player.upper()}!\n")
    sleep(1)
    print("*a big round of applause*\n")
    sleep(1)
    print("Okay, let's get started. Here's what we can do:")

def menu():
        print("\nPlease, select the option of your preference\n")
        print("1. Play")
        print("2. Scores")
        print("3. Exit\n")
        acepted_answers_menu = ["1","2","3"]
        option = input("Type your choice: ")
        if not (option in acepted_answers_menu):
            print("\n Please enter a valid option.")
            menu()
        elif option == '1':
            sleep(1)
            new_game = Game()
            new_game.intro_question()
            new_game.ask_question()
            new_game.validate_answer()
        elif option == '2':
            load_scores()
            sleep(2)
            back = input("\n\n Would you like to return to the menu or exit the program?  (menu/exit): ")
            if (back.lower() == "menu"):
                sleep(2)
                menu()
            else:
                sys.exit()
        else:
            print("")
            print(f"We hope to see you again soon {player}.")
            print("")
            sleep(2)
            sys.exit()

if __name__ == "__main__":
    main()
