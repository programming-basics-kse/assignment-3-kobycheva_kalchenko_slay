from validation import check_country, create_indexes

def overall(header, rows, teams):
    NAME, TEAM, NOC, YEAR, SPORT, MEDAL = create_indexes(header)
    medals_by_years = {}
    for team in teams:
        for row in rows:
            if row[TEAM] == team:
                medals_by_years[team] = {}
                if row[MEDAL] != 'NA':
                    if row[NAME] not in medals_by_years[team]:
                        medals_by_years[team] = {row[YEAR]: 1}
                    else:
                        medals_by_years[team][row[YEAR]] += 1
    print(medals_by_years)
    print(teams)