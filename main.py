import csv
import argparse
from medals import return_top_10_medals
from total import total
from overall import count_overall
from interactive import first_participation, interactive
from validation import check_country



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
group.add_argument('--interactive', nargs='*', help='country statistics')
parser.add_argument('--output', nargs=1, type=str, help='file to save output')
args = parser.parse_args()
result = None

if __name__ == '__main__':
    if args.medals:
        result = return_top_10_medals(categories, rows, args.medals[0], args.medals[1])

    elif args.total:
        result = total(categories, rows, args.total[0])

    elif args.overall:
        result = count_overall(categories, rows, args.overall)

    elif not args.interactive:
        args.interactive = input('Please, enter a country to get its statistics: ')
        while not check_country(rows, args.interactive):
            args.interactive = input('Please, enter valid country to get its statistics: ')
        result = interactive(categories, rows, args.interactive)

    if args.output:
        with open(args.output[0], 'w') as results_file:
            results_file.write(result)
