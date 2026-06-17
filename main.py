import random
import sys
import time
import json
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

def judgment():
    if user_score >= 18:
        print(f"==={victory_message()}===\nYou are an absolute genius!")
    elif user_score >= 12:
        print("🌟 GREAT JOB! Excellent knowledge base.")
    elif user_score >= 5:
        print("👍 NOT BAD! Good effort, keep learning!")
    elif user_score < 5 and user_score >= 2:
        print("📚 Better luck next time! Review your facts and try again.")
    elif user_score == 1:
        print("===!!! ATLEAST YOU GOT ONE 🫥===")
    elif user_score == 0:
        print("===WOW... UNIMAGINABLE!!! 🤯===")
        
print("================================")
print("--------QUIZ ENGINE GAME--------")
print("================================\n")

time.sleep(0.2)
input("Press Enter to Enter the game...")

player_name = input("\nEnter your name: ").strip()
if not player_name:
    player_name = "Player"
print(f"\nWelcome, {player_name}! To the World of Quiz!!\n")
 
print(f"Are you ready for upcoming changes {player_name}?")
n = input("Press Enter to Start or 'q' for EXIT: ").lower().strip()
if n == "q":
    time.sleep(0.1)
    print(f"\nExiting game. Goodbye! {player_name}")
    sys.exit()

time.sleep(0.4)
print("Starting Quiz", end="")
for i in range(3):
        time.sleep(0.3)
        print(".", end="")
print("\n")

all_questions = []
try:
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
except FileNotFoundError:
    print("\n❌ ERROR: Something Went Wrong!!")
    sys.exit()

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
        user_input = input("Enter your answer: ").lower().strip()
        if user_input in valid_choices:
            break   
        print("INVALID CHOICE! Please enter a, b, c, d..")
    time.sleep(0.35)
    if user_input == q["answer"]:
        print(f"\n==CORRECT==\n{victory_message()}")
        user_score += 1
    else:
        print(f"\n==WRONG==\nThe correct answer was: ({q['answer']}) {q[q['answer']]}\n")
    time.sleep(0.6)
    question_number += 1

print("\n===============================================")
print("----------------- QUIZ OVER -------------------")
print("===============================================")

print(f"\nYour Final score: {user_score}/20\n")
judgment()

HIGH_SCORE = "hiscore.json"

def load_highscore():
    try:
        with open(HIGH_SCORE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "name": "Nobody",
            "score": 0 
        }
def save_highscore(name, score):
    with open(HIGH_SCORE, "w") as file:
        json.dump(
            {
                "name": name,
                "score": score
            },
            file
        )
    
high_score_data = load_highscore()

high_score = high_score_data["score"]
high_score_name = high_score_data["name"]

if user_score > high_score:
    print(f"🎉 CONGRATULATIONS! You set a new High Score! 🎉 {player_name}\n")
    high_score = user_score
    save_highscore(player_name, user_score)
else:
    print(f"You didn't beat it!!!.\nCurrent High Score: {high_score} by {high_score_name}\n")

time.sleep(0.6)
print("======================================")
print("-------------- ENDING ----------------")
print("======================================")
