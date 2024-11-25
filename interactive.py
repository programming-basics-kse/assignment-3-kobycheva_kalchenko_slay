from validation import create_indexes


def overall(header, rows, teams):
    NAME, TEAM, NOC, YEAR, SPORT, MEDAL = create_indexes(header)
    medals_by_years = {}
    for team in teams:
        for row in rows:
            if row[TEAM] == team and row[MEDAL] != 'NA':
                if team not in medals_by_years:
                    medals_by_years[team] = {row[YEAR]: 1}
                else:
                    if row[YEAR] not in medals_by_years[team]:
                        medals_by_years[team][row[YEAR]] = 1
                    else:
                        medals_by_years[team][row[YEAR]] += 1
    return medals_by_years


def min_max_medals(header, rows, team):
    NAME, TEAM, NOC, YEAR, SPORT, MEDAL = create_indexes(header)
    team_list = [team]
    team_dict = overall(header, rows, team_list)[team]
    sorted_team_list = sorted(team_dict.items(), key=lambda x: x[1])
    min_medals = sorted_team_list[0]
    max_medals = sorted_team_list[-1]
    output = f'\nThe lowest medals number is {min_medals[1]} in {min_medals[0]}'
    for element in sorted_team_list[1:]:
        if element[1] == min_medals[1]:
            output += f', {element[0]} year'
    output += f'\nThe biggest medals number is {max_medals[1]} in {max_medals[0]}'
    for element in sorted_team_list[:-1]:
        if element[1] == max_medals[1]:
            output += f', {element[0]} year'
    return output


def first_participation(header, rows, team):
    NAME, TEAM, NOC, YEAR, SPORT, MEDAL = create_indexes(header)
    PLACE = header.index('City')
    # sorted_years = sorted({row[YEAR] for row in rows})
    years_places_list = []
    for row in rows:
        if row[TEAM] == team:
            if [row[YEAR], row[PLACE]] not in years_places_list:
                years_places_list.append([row[YEAR], row[PLACE]])
    year_places_sorted = sorted(years_places_list, key=lambda x: x[0])
    number_of_participation = len(year_places_sorted)
    output = f'First participation in Olympics was in {year_places_sorted[0][0]} year in {year_places_sorted[0][1]}'
    return output, number_of_participation


def average_number(header, rows, team, number_of_participation):
    NAME, TEAM, NOC, YEAR, SPORT, MEDAL = create_indexes(header)
    medals_dict = {}
    for row in rows:
        if row[TEAM] == team and row[MEDAL] != 'NA':
            if row[MEDAL] not in medals_dict:
                medals_dict[row[MEDAL]] = 1
            else:
                medals_dict[row[MEDAL]] += 1
    output = f'\nAverage number of Gold medals is {round(medals_dict['Gold'] / number_of_participation)}'
    output += f', Silver - {round(medals_dict['Silver'] / number_of_participation)}'
    output += f', Bronze - {round(medals_dict['Bronze'] / number_of_participation)}'
    return output


def interactive(header, rows, team):
    first, participation_number = first_participation(header, rows, team)
    min_max = min_max_medals(header, rows, team)
    average = average_number(header, rows, team, participation_number)
    output = first + min_max + average
    print(output)
    return output
