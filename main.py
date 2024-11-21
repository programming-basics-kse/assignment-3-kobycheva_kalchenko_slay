import csv
from lib2to3.pgen2.tokenize import group

def open_file():
    with open("athlete_events.csv", "r") as file:
        reader = csv.reader(file)
        rows = []
        header = next(reader)
        for row in reader:
            rows.append(row)
    return header, rows

categories, rows = open_file()

if __name__ == '__main__':
    print(categories, rows[81])