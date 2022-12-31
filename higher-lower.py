from art import logo, vs
from game_data import data
import random as r
print(logo)



CORRECT = 1
WRONG = 0



def to_compare():
    a = data[r.randint(0, 49)]
    b = data[r.randint(0,49)]

    print(f"Compare A: {a.get('name')}, a {a.get('description')}, from {a.get('country')}.")
    print(vs)
    print(f"Against B: {b.get('name')}, a {b.get('description')}, from {b.get('country')}.")

    ANSWER = input("Who has more followers? Type 'A' or 'B': ")

    if ANSWER == 'A' or ANSWER == 'a':
        if a.get("follower_count") > b.get("follower_count"):
            print("Correct!")
            return CORRECT
        elif a.get("follower_count") == b.get("follower_count"):
            print("Correct!")
            return CORRECT
        else:
            print("Wrong!")
            return WRONG

    elif ANSWER == 'B' or ANSWER == 'b' :
        if b.get("follower_count")> a.get("follower_count"):
            print("Correct!")
            return CORRECT
        elif b.get("follower_count") == a.get("follower_count"):
            print("Correct!")
            return CORRECT
        else:
            print("Wrong!")
            return WRONG
    else:
        print("Not valid.")
        return WRONG

def increase():
    score = 0
    if 1 == 1:
        while score >= 0:
            print(f"Your score: {score}\n")
            x = to_compare()  #1 or 0
            if x == 0:
                print(f"Game Over!! Your final score is {score}")
                break
            else:
                score+=x
                continue
          
increase()