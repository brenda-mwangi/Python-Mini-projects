# Dictionary comprehension
# method 1: new_dict = {new_key:new_value for item in list}
# method 2: new_dict = {new_key:new_value for (key,value) in dict.items()}
# method 3: new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
names = ["Alex","Beth","Caroline", "Dave", "Eleanor", "Freddie"]

# # method 1
# score = random.randint(40,95)
# student_scores = {student:random.randint(40,75) for student in names}
# print(student_scores)

# # method 3
# passed = {student:score for (student,score) in student_scores.items() if score>=60}
# print(passed)

# working with dataframes
import pandas as pd
student_scores = {
    'student ': names,
    'score':[52, 67, 64, 67, 68, 46]
    }
student_df = pd.DataFrame(student_scores)
# loop through df rows
for (index, row) in student_df.iterrows():
    print(row.student)