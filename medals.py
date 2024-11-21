def top_10_medals(header, rows, team, year):
    NAME = header.index('Name')
    TEAM = header.index('Team')
    NOC = header.index('NOC')
    YEAR = header.index('Year')
    SPORT = header.index('Sport')
    MEDAL = header.index('Medal')

    sportsman_total = {}
    sportsman_medals = {}

    for row in rows:
        if (team == row[TEAM] or team == row[NOC] or team in row[TEAM].split('/')) and year == row[YEAR]:
            if row[MEDAL] != 'NA':
                if row[NAME] not in sportsman_medals:
                    sportsman_medals[row[NAME]] = {'discipline': None, 'Gold' : 0, 'Silver' : 0, 'Bronze' : 0}
                sportsman_medals[row[NAME]][row[MEDAL]] += 1
                sportsman_medals[row[NAME]]['discipline'] = row[SPORT]
                if row[NAME] not in sportsman_total:
                    sportsman_total[row[NAME]] = 0
                sportsman_total[row[NAME]] += 1
    top_10 = sorted(sportsman_total.items(), key=lambda x: x[1], reverse=True)[:10]

    for tuple in top_10:
        name = tuple[0]
        print(f'{name},  {sportsman_medals[name]['discipline']},  Gold: {sportsman_medals[name]['Gold']},  Silver: {sportsman_medals[name]['Silver']} ,  Bronze: {sportsman_medals[name]['Bronze']}')