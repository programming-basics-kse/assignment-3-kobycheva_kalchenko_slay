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
    print(f'Total gold medals for country: {total_gold}, silver: {total_silver}, bronze: {total_bronze}')

def check_year(rows, year):
    valid_years = {row[9] for row in rows}
    if str(year) not in valid_years:
        print('No Olympics this year')
        return False
    return True

def check_country(rows, team):
    valid_teams = {row[6] for row in rows}
    valid_nocs = {row[7] for row in rows}
    if team not in (valid_teams or valid_nocs):
        print('This country does not exict')
        return False
    return True

def top_10_medals(header, rows, team, year):
    NAME = header.index('Name')
    TEAM = header.index('Team')
    NOC = header.index('NOC')
    YEAR = header.index('Year')
    SPORT = header.index('Sport')
    MEDAL = header.index('Medal')
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
                    else:
                        sportsman_medals[row[NAME]][row[MEDAL]] += 1
                sportsman_medals[row[NAME]]['Discipline'] = row[SPORT]
                if row[NAME] not in sportsman_total:
                    sportsman_total[row[NAME]] = 0
                sportsman_total[row[NAME]] += 1
    top_10 = sorted(sportsman_total.items(), key=lambda x: x[1], reverse=True)[:10]
    print(f"Top 10 sportsmen for {team} in {year}:")
    for result in top_10:
        print(f"{top_10.index(result) + 1}) {result[0]}")
        for key, value in sportsman_medals[result[0]].items():
            print(f'   {key}: {value}')
    count_medals(sportsman_medals)
