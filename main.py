import csv
import argparse
from medals import creating_dicts, return_top_10_medals
from total import total
from overall import overall

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
group.add_argument('--overall', nargs='+', type=str, help='the most productive year for this country')
parser.add_argument('--output', nargs=1, type=str, help='file to save output')
args = parser.parse_args()
result = None

if __name__ == '__main__':
    if args.medals:
        result = return_top_10_medals(categories, rows, args.medals[0], args.medals[1])

    elif args.total:
        result = total(categories, rows, args.total[0])

    elif args.overall:
        result = overall(categories, rows, args.overall)

    if args.output:
        with open(args.output[0], 'w') as results_file:
            results_file.write(result)