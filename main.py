import random
import sys
import time
import json

"""
========================================
---------- Quiz Engine System ----------
========================================

Rules:
    - Press Enter to begin the game.
    - Enter your name to personalize your scoreboard tracker, if not entered engine will consider it as 'Player'.
    - The full question bank contains 50 diverse questions.
    - Every individual game session will randomly select exactly 20 questions.
    - Options will always be 'a', 'b', 'c', or 'd'.
    - Inputs are case-insensitive ('A' and 'a' both work).
    - Invalid inputs do not cost a turn; you will be prompted to try again.

Scoring:
    - Each correct answer awards 1 point.
    - No points are deducted for wrong answers.
    - A summary, final score, and accuracy percentage will display at the end.

"""


class Utils:

    @staticmethod
    def loading():
        for i in range(3):
            time.sleep(0.3)
            print(".", end = "", flush=True)

    @staticmethod
    def victory_message():
        word_pool = [
            "!!FABULOUS!!",
            "!!EXTRAORDINARY!!",
            "!!!WONDERFUL!!!",
            "!!MARVELOUS!!",
            "!!SPECTACULAR!!",
            "!!SUPERB!!",
            "!!!FANTASTIC!!!",
            "!!AMAZING!!",
            "!!PHENOMENAL!!",
            "!!SPLENDID!!",
            "!!TERRIFIC!!",
            "!!OUTSTANDING!!",
            "!!STUPENDOUS!!",
        ]

        random_word = random.choice(word_pool)
        return random_word

    @staticmethod
    def judgment(score):
        if score >= 18:
            print(f"==={Utils.victory_message()}===\nYou are an absolute genius!")
        elif score >= 12:
            print("🌟 GREAT JOB! Excellent knowledge base.")
        elif score >= 5:
            print("👍 NOT BAD! Good effort, keep learning!")
        elif score >= 2:
            print("📚 Better luck next time! Review your facts and try again.")
        elif score == 1:
            print("===!!! ATLEAST YOU GOT ONE 🫥===")
        elif score == 0:
            print("===WOW... UNIMAGINABLE!!! 🤯===")

    @staticmethod
    def user_percentage(score):
        percentage = (score / 20) * 100
        percentage = int(percentage)
        print("Score: ", end="")
        for i in range(percentage // 5):
            time.sleep(0.1)
            print("◼", end="", flush=True)
        print(f" {percentage}%")


class Quiz_view:

    @staticmethod
    def start():
        print("================================")
        print("--------QUIZ ENGINE GAME--------")
        print("================================\n")

    @staticmethod
    def over():
        print("\n===============================================")
        print("----------------- QUIZ OVER -------------------")
        print("===============================================")

    @staticmethod
    def end():
        print("======================================")
        print("-------------- ENDING ----------------")
        print("======================================")


Quiz_view.start()
time.sleep(0.4)
input("Press Enter to Enter the game...")
time.sleep(0.5)

player_name = input("\nEnter your name: ").strip()
if not player_name:
    player_name = "Player"
time.sleep(0.3)
Utils.loading()
print(f"\nWelcome, {player_name}! To the World of Quiz!!\n")
time.sleep(0.35)
print(f"Are you ready for upcoming changes {player_name}?")
start_choice = input("Press Enter to Start or 'q' for EXIT: ").lower().strip()
if start_choice == "q":
    time.sleep(0.2)
    Utils.loading()
    print(f"\nExiting game. Goodbye! {player_name}")
    sys.exit()

time.sleep(0.4)
print("Starting Quiz", end="")
Utils.loading()
print("\n")

all_questions = []
QUESTION_BANK = "question_bank.txt"
QUESTION_LENGTH = 20
try:
    with open(QUESTION_BANK, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

        for i in range(0, len(lines), 6):
            if i + 5 >= len(lines):
                print(f"WARNING: Incomplete question at line {i}. Skipping...")
                break

            question_dict = {
                "question": lines[i],
                "a": lines[i + 1],
                "b": lines[i + 2],
                "c": lines[i + 3],
                "d": lines[i + 4],
                "answer": lines[i + 5].lower(),
            }
            all_questions.append(question_dict)
except FileNotFoundError:
    Utils.loading()
    print("\nERROR: Something Went Wrong!!")
    time.sleep(0.4)
    sys.exit()
except Exception as e:
    Utils.loading()
    print(f"\nERROR: Unexpected error - {e}")
    time.sleep(0.4)
    sys.exit()

if len(all_questions) < QUESTION_LENGTH:
    Utils.loading()
    time.sleep(0.35)
    print("Something Went Wrong!!")
    sys.exit()
quiz_session = random.sample(all_questions, QUESTION_LENGTH)

user_score = 0
question_number = 1
valid_choices = ["a", "b", "c", "d"]

for q in quiz_session:
    print(f"\nQ: {question_number}/{QUESTION_LENGTH}")
    print(f" {q['question']}\n")
    print(f"    a) {q['a']}")
    print(f"    b) {q['b']}")
    print(f"    c) {q['c']}")
    print(f"    d) {q['d']}")

    while True:
        user_input = input("Enter your answer: ").lower().strip()
        if user_input in valid_choices:
            break
        print("INVALID CHOICE! Please enter a, b, c, d..")
    time.sleep(0.35)
    if user_input == q["answer"]:
        print("\n==CORRECT==")
        user_score += 1
    else:
        print(
            f"\n==WRONG==\nThe correct answer was: ({q['answer']}) {q[q['answer']]}\n"
        )
    time.sleep(0.6)
    question_number += 1
time.sleep(0.5)

Quiz_view.over()

print(f"\nYour Final score: {user_score}/{QUESTION_LENGTH}\n")
Utils.judgment(user_score)
time.sleep(0.4)
Utils.user_percentage(user_score)

HIGH_SCORE = "hiscore.json"


def load_highscore():
    try:
        with open(HIGH_SCORE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"name": "Nobody", "score": 0}


def save_highscore(name, score):
    with open(HIGH_SCORE, "w") as file:
        json.dump({"name": name, "score": score}, file)


high_score_data = load_highscore()

high_score = high_score_data["score"]
high_score_name = high_score_data["name"]

if user_score > high_score:
    print(f"🎉 CONGRATULATIONS! You set a new High Score! 🎉 {player_name}\n")
    high_score = user_score
    save_highscore(player_name, user_score)
else:
    print(
        f"You didn't beat it!!!.\n🏆Current Champion: {high_score_name} ({high_score}/{QUESTION_LENGTH})\n"
    )

time.sleep(0.6)
Quiz_view.end()
