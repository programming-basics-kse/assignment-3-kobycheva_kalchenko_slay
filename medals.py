from validation import check_country, check_year, create_indexes

def creating_dicts(header, rows, team, year):
    NAME, TEAM, NOC, YEAR, SPORT, MEDAL = create_indexes(header)
    total_by_sportsman = {}
    medals_by_sportsman = {}
    for row in rows:
        if (team == row[TEAM] or team == row[NOC] or team in row[TEAM].split('/')) and str(year) == row[YEAR]:
            if row[MEDAL] != 'NA':
                if row[NAME] not in medals_by_sportsman:
                    medals_by_sportsman[row[NAME]] = {row[SPORT]: {row[MEDAL]: 1}}
                else:
                    if row[SPORT] not in medals_by_sportsman[row[NAME]]:
                        medals_by_sportsman[row[NAME]][row[SPORT]] = {row[MEDAL]: 1}
                    else:
                        if row[MEDAL] not in medals_by_sportsman[row[NAME]][row[SPORT]]:
                            medals_by_sportsman[row[NAME]][row[SPORT]][row[MEDAL]] = 1
                        else:
                            medals_by_sportsman[row[NAME]][row[SPORT]][row[MEDAL]] += 1
                if row[NAME] not in total_by_sportsman:
                    total_by_sportsman[row[NAME]] = 0
                total_by_sportsman[row[NAME]] += 1
    return medals_by_sportsman, total_by_sportsman

def count_medals(medals_dict):
    total_gold = 0
    total_silver = 0
    total_bronze = 0
    for name in medals_dict:
        for sport in medals_dict[name]:
            if 'Gold' in medals_dict[name][sport]:
                total_gold += medals_dict[name][sport]['Gold']
            elif 'Silver' in medals_dict[name][sport]:
                total_silver += medals_dict[name][sport]['Silver']
            else:
                total_bronze += medals_dict[name][sport]['Bronze']
    return total_gold + total_silver + total_bronze, f'Total gold medals for country: {total_gold}, silver: {total_silver}, bronze: {total_bronze}'

def return_top_10_medals(header, rows, team, year):
    if not check_year(rows, year) or not check_country(rows, team):
        exit()
    medals_by_sportsman, total_by_sportsman = creating_dicts(header, rows, team, year)
    number_of_medals, total_count_output = count_medals(medals_by_sportsman)
    if number_of_medals < 10:
        output = f'Only {number_of_medals} medals of this country'
        print(output)
        return output
    top_10 = sorted(total_by_sportsman.items(), key=lambda x: x[1], reverse=True)[:10]
    output = f"Top 10 sportsmen for {team} in {year}:\n"
    for result in top_10:
        output += f"{top_10.index(result) + 1}: {result[0]}\n"
        for sport, medal_dict in medals_by_sportsman[result[0]].items():
            sport_line = f'{sport} '
            for medal, amount in medal_dict.items():
                sport_line += f" {medal}: {amount}"
            output += sport_line + '\n'
    output += total_count_output
    print(output)
    return output
