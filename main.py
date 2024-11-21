import csv
import argparse
from medals import top_10_medals

def open_file():
    with open("athlete_events.csv", "r") as file:
        reader = csv.reader(file)
        rows = []
        header = next(reader)
        for row in reader:
            rows.append(row)
    return header, rows


categories, rows = open_file()

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--medals', nargs=2, help='top 10 medalists of selected country')
group.add_argument('--total', nargs=1, type=int, help='country medals in this year')
parser.add_argument('--output', nargs=1, type=str, help='file to save output')
args = parser.parse_args()

if __name__ == '__main__':
    if args.medals:
        top_10_medals(categories, rows, args.medals[0], args.medals[1])


