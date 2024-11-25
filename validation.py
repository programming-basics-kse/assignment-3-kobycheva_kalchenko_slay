def check_year(rows, year):
    valid_years = {row[9] for row in rows}
    if str(year) not in valid_years:
        print(f'No Olympics on year {year}')
        return False
    return True


def check_country(rows, team):
    valid_teams = {row[6] for row in rows}
    valid_nocs = {row[7] for row in rows}
    if team in valid_teams or team in valid_nocs:
        return True
    print(f'Country {team} does not exist')
    return False

def create_indexes(header):
    return header.index('Name'), header.index('Team'), header.index('NOC'), header.index('Year'), header.index('Sport'), header.index('Medal')