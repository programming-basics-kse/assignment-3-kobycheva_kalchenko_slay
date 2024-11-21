
def top_10_medals(header, rows, team, year):
    NAME = header.index('Name')
    TEAM = header.index('Team')
    NOC = header.index('NOC')
    YEAR = header.index('Year')
    SPORT = header.index('Sport')
    MEDAL = header.index('Medal')

    sportsman_dict = {}
    for row in rows:
        if (team == row[TEAM] or team == row[NOC] or team in row[TEAM].split('/')) and year == row[YEAR]:
            if row[MEDAL] != 'NA':
                if row[NAME] not in sportsman_dict:
                    sportsman_dict[row[NAME]] = {'total' : 0, 'Gold' : 0, 'Silver' : 0, 'Bronze' : 0}
                    for key in sportsman_dict[row[NAME]]:
                        if key == row[MEDAL]:
                            sportsman_dict[row[NAME]][key] += 1
                            sportsman_dict[row[NAME]]['total'] += 1
                else:
                    for key in sportsman_dict[row[NAME]]:
                        if key == row[MEDAL]:
                            sportsman_dict[row[NAME]][key] += 1
                            sportsman_dict[row[NAME]]['total'] += 1
    top_gold = max(sportsman_dict.items(), key=lambda x: x[1])[1]
    print(sportsman_dict)
    print(top_gold)















