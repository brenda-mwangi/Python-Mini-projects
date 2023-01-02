from art import logo, vs
from game_data import data
import random as r
from replit import clear

CORRECT = 1
WRONG = 0

def to_compare(a, b):
    while a == b:
        b = data[r.randint(0,49)]

    print(f"Compare A: {a.get('name')}, a {a.get('description')}, from {a.get('country')}.")
    print(vs)
    print(f"Against B: {b.get('name')}, a {b.get('description')}, from {b.get('country')}.")
    print(f"{a.get('name')}: {a.get('follower_count')}")
    print(f"{b.get('name')}: {b.get('follower_count')}")

    answer = (input("Who has more followers? Type 'A' or 'B': ")).lower()

    def check(answer):
        if answer == 'A' or answer == 'a':
            if a.get("follower_count") > b.get("follower_count"):
                return CORRECT
            elif a.get("follower_count") == b.get("follower_count"):
                return CORRECT
            else:
                return WRONG

        elif answer == 'b' :
            if b.get("follower_count")> a.get("follower_count"):
                return CORRECT
            elif b.get("follower_count") == a.get("follower_count"):
                return CORRECT
            else:
                return WRONG
        else:
            print("Not valid.")
            return WRONG
            
    return check(answer)

def increase():
    score = 0
    if 1 == 1:
        while score >= 0:
            clear()
            print(logo)
            print(f"Your score: {score}\n")
            x = to_compare(a = data[r.randint(0, 49)], b = data[r.randint(0,49)])  #1 or 0
            if x == 0:
                print(f"Game Over!! Your final score is {score}")
                break
            else:
                score+=x 
                print("Correct!")
                continue

increase()