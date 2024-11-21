
def open_file():
    with open("Olympic Athletes - athlete_events.tsv", "r") as file:
        heading = next(file).replace('\n', '')
        heading = heading.split('\t')
        next_line = file.readline()
        lines = []
        while next_line:
            split = next_line.split('\t')
            lines.append(split)
            next_line = file.readline()
        for line in lines:
            line[-1] = line[-1].replace('\n','')
    return heading, lines

categories, rows = open_file()

if __name__ == '__main__':
    print(categories, rows[0])
