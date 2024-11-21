from medals import check_year

def total(header, rows, year):
    NOC = header.index('NOC')
    YEAR = header.index('Year')
    MEDAL = header.index('Medal')
    total_medals_per_country = {}
    if not check_year(rows, year):
        exit()
    for row in rows:
        if row[YEAR] == str(year):
            if row[MEDAL] != 'NA':
                if row[NOC] not in total_medals_per_country:
                    total_medals_per_country[row[NOC]] = ''
                if row[MEDAL] not in total_medals_per_country[row[NOC]]:
                    total_medals_per_country[row[NOC]] += f'{row[MEDAL]} - '
    output = ''
    for key, value in total_medals_per_country.items():
        print(f"{key}: {value[:-3]}")
        output += f"{key}: {value[:-3]}\n"
    return output