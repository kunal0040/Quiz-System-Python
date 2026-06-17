import random
import sys
import time
'''
========================================
---------- Quiz Engine System ----------
========================================

Rules:
    - Press [SPACEBAR] and hit Enter to begin the game.
    - Enter your name to personalize your scoreboard tracker.
    - The full question bank contains 50 diverse questions.
    - Every individual game session will randomly select exactly 20 questions.
    - Options will always be 'a', 'b', 'c', or 'd'.
    - Inputs are case-insensitive ('A' and 'a' both work).
    - Invalid inputs do not cost a turn; you will be prompted to try again.

Scoring:
    - Each correct answer awards 1 point.
    - No points are deducted for wrong answers.
    - A summary, final score, and accuracy percentage will display at the end.

'''
def loading():
    for i in range(3):
        time.sleep(0.3)
        print(".", end="")


print("================================")
print("--------QUIZ ENGINE GAME--------")
print("================================\n")

time.sleep(0.2)
input("Press Enter to Enter the game...")

player_name = input("\nEnter your name: ").strip()
if not player_name:
    player_name = "Player"
print(f"\nWelcome, {player_name}! To the World of Quiz!!\n")
 
print(f"Are or ready for upcoming changes {player_name}?")
n = input("Press Enter to Start or 'q' for EXIT: ").lower().strip()
if n == "q":
    time.sleep(0.1)
    print(f"\nExiting game. Goodbye! {player_name}")
    sys.exit()

time.sleep(0.4)
print("Starting Quiz", end="")
loading()
print()

all_questions = []
with open("question_bank.txt", "r") as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]

    for i in range(0, len(lines), 6):
        question_dict = {
            "question": lines[i],
            "a": lines[i+1],
            "b": lines[i+2],
            "c": lines[i+3],
            "d": lines[i+4],
            "answer": lines[i+5].lower()
        }
        all_questions.append(question_dict)

quiz_session = random.sample(all_questions, 20)

user_score = 0
question_number = 1
valid_choices = ["a", "b", "c", "d"]

for q in quiz_session:
    print(f"\nQ: {question_number}/20")
    print(f" {q['question']}\n")
    print(f"    a) {q['a']}")
    print(f"    b) {q['b']}")
    print(f"    c) {q['c']}")
    print(f"    d) {q['d']}")

while True:
    user_input = input("Enter you answer: ").lower().strip()
    if user_input in valid_choices:
        break   
    print("INVALID CHOICE! Please enter a, b, c, d..")