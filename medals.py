from validation import check_country, check_year, create_indexes

def count_medals(medals_dict):
    total_gold = 0
    total_silver = 0
    total_bronze = 0
    for name in medals_dict:
        if 'Gold' in medals_dict[name]:
            total_gold += medals_dict[name]['Gold']
        elif 'Silver' in medals_dict[name]:
            total_silver += medals_dict[name]['Silver']
        else:
            total_bronze += medals_dict[name]['Bronze']
    return total_gold + total_silver + total_bronze, f'Total gold medals for country: {total_gold}, silver: {total_silver}, bronze: {total_bronze}'

def top_10_medals(header, rows, team, year):
    NAME, TEAM, NOC, YEAR, SPORT, MEDAL = create_indexes(header)
    sportsman_total = {}
    sportsman_medals = {}
    if not check_year(rows, year) or not check_country(rows, team):
        exit()
    for row in rows:
        if (team == row[TEAM] or team == row[NOC] or team in row[TEAM].split('/')) and str(year) == row[YEAR]:
            if row[MEDAL] != 'NA':
                if row[NAME] not in sportsman_medals:
                    sportsman_medals[row[NAME]] = {'Discipline': None}
                if row[MEDAL] not in sportsman_medals[row[NAME]]:
                    sportsman_medals[row[NAME]][row[MEDAL]] = 1
                    sportsman_medals[row[NAME]]['Discipline'] = row[SPORT]
                else:
                    sportsman_medals[row[NAME]][row[MEDAL]] += 1
                    sportsman_medals[row[NAME]]['Discipline'] += row[SPORT]

                if row[NAME] not in sportsman_total:
                    sportsman_total[row[NAME]] = 0
                sportsman_total[row[NAME]] += 1

    number_of_medals, total_count_output = count_medals(sportsman_medals)
    if number_of_medals < 10:
        output = f'Only {number_of_medals} medals of this country'
        print(output)
        return output
    top_10 = sorted(sportsman_total.items(), key=lambda x: x[1], reverse=True)[:10]
    output = f"Top 10 sportsmen for {team} in {year}:\n"
    for result in top_10:
        output += f"{top_10.index(result) + 1}: {result[0]}\n"
        for key, value in sportsman_medals[result[0]].items():
            output += f"{key}: {value}\n"
    output += total_count_output
    print(output)
    return output
