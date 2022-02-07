import csv
with open('file2.csv')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row[0]+""+row[1])
