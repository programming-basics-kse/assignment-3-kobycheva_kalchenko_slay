def convert_input(player_list):
    ages = []
    sex = []
    age_category_dict = {1: range(18, 26), 2: range(26, 36), 3: range(36, 51), 4: range(51, 90)}
    for element in player_list:
        if element == 'M' or element == 'F':
            sex.append(element)
        elif int(element) in age_category_dict:
            ages.append([str(x) for x in age_category_dict[int(element)]])
    return ages, sex


def create_top_player_dict(header, rows, ages, sexes):
    AGE, SEX, NAME, MEDAL = header.index('Age'), header.index('Sex'), header.index('Name'), header.index('Medal')
    sportsman_dict = {}
    for row in rows:
        for sex in sexes:
            for age in ages:
                short_age = f'{age[0]} - {age[-1]}'
                if row[MEDAL] != 'NA' and row[AGE] in age and row[SEX] == sex:
                    if sex not in sportsman_dict:
                        sportsman_dict[sex] = {short_age: {row[NAME]: 1}}
                    else:
                        if short_age not in sportsman_dict[sex]:
                            sportsman_dict[sex][short_age] = {row[NAME]: 1}
                        else:
                            if row[NAME] not in sportsman_dict[sex][short_age]:
                                sportsman_dict[sex][short_age][row[NAME]] = 1
                            else:
                                sportsman_dict[sex][short_age][row[NAME]] += 1
    return sportsman_dict


def best_participant(header, rows, player_list):
    age_categories, sexes = convert_input(player_list)
    player_medals_dict = create_top_player_dict(header, rows, age_categories, sexes)
    output = ''
    for sex in sexes:
        for age in age_categories:
            short_age = f'{age[0]} - {age[-1]}'
            top_1 = sorted(player_medals_dict[sex][short_age].items(), key=lambda x: x[1])[-1]
            output += f'\nIn {sex} sex in age group {short_age} years best sportsman is {top_1[0]} with {top_1[1]} medals'
    print(output)
    return output
