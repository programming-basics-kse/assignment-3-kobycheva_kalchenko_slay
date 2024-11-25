from validation import check_country, create_indexes

def overall_create_dict(header, rows, teams):
    NAME, TEAM, NOC, YEAR, SPORT, MEDAL = create_indexes(header)
    medals_by_years = {}
    for team in teams:
        if not check_country(rows, team):
            exit()
        for row in rows:
            if (row[TEAM] == team or row[NOC] == team) and row[MEDAL] != 'NA':
                if team not in medals_by_years:
                    medals_by_years[team] = {row[YEAR]: 1}
                else:
                    if row[YEAR] not in medals_by_years[team]:
                        medals_by_years[team][row[YEAR]] = 1
                    else:
                        medals_by_years[team][row[YEAR]] += 1
        return medals_by_years

def overall_count_overall(medals_by_years):
    output = ""
    for team in medals_by_years:
        team_list = medals_by_years[team]
        top_year = sorted(team_list.items(), key=lambda x: x[1], reverse=True)[:1]
        for key, value in top_year:
            output += f"The most successful year for {team} was {key} with {value} medals \n"
    print(output)
    return output