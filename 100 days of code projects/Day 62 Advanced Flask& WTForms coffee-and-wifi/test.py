import csv

with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

for cafe in list_of_rows:
    for i in range(len(cafe)):
        print(cafe[i])
