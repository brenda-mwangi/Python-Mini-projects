# {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato():
    user_input = input("Enter your a word: ").upper()
    try:
        output_list = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato()
    else:
        print(output_list)
nato()

