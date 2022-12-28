from art import logo, vs
from game_data import data
import random as r
# print(logo)


A = data[r.randint(0, 49)]
B = data[r.randint(0,49)]
# ANSWER = input("Who has more followers? Type 'A' or 'B': ")
CORRECT = 1
WRONG = 0
# print(A)
# print(B)
def increase():
    i = 0
    

def to_compare():
    print(f"Compare A: {A.get('name')}, a {A.get('description')}, from {A.get('country')}.")
    print(vs)
    print(f"Against B: {B.get('name')}, a {B.get('description')}, from {B.get('country')}.")
    # print(A.get("follower_count"))
    # print(B.get("follower_count"))
    ANSWER = input("Who has more followers? Type 'A' or 'B': ")


# def compare_answer():
    if ANSWER == 'A' or ANSWER == 'a':
        if A.get("follower_count") > B.get("follower_count"):
            print("Correct!")
            return CORRECT
        else:
            print("Wrong!")
            return WRONG

    elif ANSWER == 'B' or ANSWER == 'b' :
        if B.get("follower_count")> A.get("follower_count"):
            return CORRECT
        else:
            return WRONG
    else:
        print("Not valid.")

to_compare()
