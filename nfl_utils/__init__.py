import re
import requests
from bs4 import BeautifulSoup

'''Variables'''
career_stats = 1
game_log = 2
situational_stats = 3
class_even = 'even'
class_odd = 'odd'

def make_team_url(team_name):
    print('Making ' + team_name + ' URL...')
    team_name = team_name.lower()
    team_url = "http://www.nfl.com/teams/roster?team="

    cardinals = "ARZ"
    falcons = "ATL"
    ravens = "BAL"
    bills = "BUF"
    panthers = "CAR"
    bears = "CHI"
    bengals = "CIN"
    browns = "CLE"
    cowboys = "DAL"
    broncos = "DEN"
    lions = "DET"
    packers = "GB"
    texans = "HOU"
    colts = "IND"
    jaguars = "JAC"
    chiefs = "KC"
    chargers = "LAC"
    rams = "LA"
    dolphins = "MIA"
    vikings = "MIN"
    patriots = "NE"
    saints = "NO"
    giants = "NYG"
    jets = "NYJ"
    raiders = "OAK"
    eagles = "PHI"
    steelers = "PIT"
    fortyniners = "SF"
    seahawks = "SEA"
    buccaneers = "TB"
    titans = "TEN"
    redskins = "WAS"

    if team_name == 'cardinals':
        team_url += cardinals
        return team_url
    elif team_name == 'falcons':
        team_url += falcons
        return team_url
    elif team_name == 'ravens':
        team_url += ravens
        return team_url
    elif team_name == 'bills':
        team_url += bills
        return team_url
    elif team_name == 'panthers':
        team_url += panthers
        return team_url
    elif team_name == 'bears':
        team_url += bears
        return team_url
    elif team_name == 'bengals':
        team_url += bengals
        return team_url
    elif team_name == 'browns':
        team_url += browns
        return team_url
    elif team_name == 'cowboys':
        team_url += cowboys
        return team_url
    elif team_name == 'broncos':
        team_url += broncos
        return team_url
    elif team_name == 'lions':
        team_url += lions
        return team_url
    elif team_name == 'packers':
        team_url += packers
        return team_url
    elif team_name == 'texans':
        team_url += texans
        return team_url
    elif team_name == 'colts':
        team_url += colts
        return team_url
    elif team_name == 'jaguars':
        team_url += jaguars
        return team_url
    elif team_name == 'chiefs':
        team_url += chiefs
        return team_url
    elif team_name == 'chargers':
        team_url += chargers
        return team_url
    elif team_name == 'rams':
        team_url += rams
        return team_url
    elif team_name == 'dolphins':
        team_url += dolphins
        return team_url
    elif team_name == 'vikings':
        team_url += vikings
        return team_url
    elif team_name == 'patriots':
        team_url += patriots
        return team_url
    elif team_name == 'saints':
        team_url += saints
        return team_url
    elif team_name == 'giants':
        team_url += giants
        return team_url
    elif team_name == 'jets':
        team_url += jets
        return team_url
    elif team_name == 'raiders':
        team_url += raiders
        return team_url
    elif team_name == 'eagles':
        team_url += eagles
        return team_url
    elif team_name == 'steelers':
        team_url += steelers
        return team_url
    elif team_name == 'fortyniners':
        team_url += fortyniners
        return team_url
    elif team_name == 'seahawks':
        team_url += seahawks
        return team_url
    elif team_name == 'buccaneers':
        team_url += buccaneers
        return team_url
    elif team_name == 'titans':
        team_url += titans
        return team_url
    elif team_name == 'redskins':
        team_url += redskins
    print('Team URL created...')
    return team_url


#process player links and return a dictionary containing the player name and a list of links
def process_player_link(soup):
    print('Processing player links...')
    #find_position = re.compile(r'[<td>]\s*(rb|wr|te|qb|k)\s*[</td>]\s*', re.IGNORECASE)

    find_name_link = re.compile(r'<td\s*style="text-align:\w*">\s*<a\s*href="/player/\w+\.*\w*\.*\w*/\d*/profile">\s*', re.IGNORECASE)
    players_at_position = {}
    player_links = []
    td_counter = 0
    class_name_array = ['odd', 'even']

    for class_name in class_name_array:

        for get_tr in soup.find_all('tr', class_=class_name):
            for td in get_tr.find_all('td'):
                make_string = str(td)

                if td_counter == 1:

                    # condition position
                    position = get_position(make_string)
                    player_links.append(position)
                    player_links.append(career_stat_url)
                    player_links.append(game_log_url)
                    player_links.append(situational_stats_url)
                    players_at_position[player_name] = player_links
                    player_links = []
                    td_counter = 0

                #position_found = re.search(find_position, make_string)
                name_found = re.search(find_name_link, make_string)
                if (name_found):

                    td_counter = 1
                    # condition name
                    player_name = get_name(make_string)

                    # get links
                    career_stat_url = make_player_link(make_string, career_stats)
                    game_log_url = make_player_link(make_string, game_log)
                    situational_stats_url = make_player_link(make_string, situational_stats)
    print('Player links created...')
    return (players_at_position)

''' SPLITTING FUNCTIONS
    # split needs to be done this way because
    # if you use a multi param split it will split
    # on the first instance of < tag

    # split current string on > tag
'''

def get_name(name_line):

    split_string = name_line.split('>')
    split_one = str(split_string[2])

    # Then split on < tag
    split_two = split_one.split('<')
    return(split_two[0])

def get_position(position_line):

    split_string = position_line.split('>')
    split_one = str(split_string[1])

    # Then split on < tag
    split_two = split_one.split('<')
    return(split_two[0])

def make_player_link(link_line, page):

    player_stat_url = 'http://www.nfl.com/player/'

    split_string = link_line.split('>')
    split_one = str(split_string[1])
    split_two= split_one.split('/')
    p_name = str(split_two[2])
    id_num = str(split_two[3])
    player_stat_url+=p_name + '/' + id_num + '/'

    if(page == career_stats):
        player_stat_url+='careerstats'
        return player_stat_url

    elif(page == game_log):
        player_stat_url+='gamelogs'
        return player_stat_url

    elif(page == situational_stats):
        player_stat_url+='situationalstats'
        return player_stat_url

    else:
        return(0) #return error


#TODO: Move this to new game to game util if necessary
def process_years_in_league(player_link_dict):
    print('Processing player years in league...')
    year_array = []
    player_years = {}

    for key, value in player_link_dict.items():

     # print(value[1])
        get_game_log_main = requests.get(value[2])
        career_soup = BeautifulSoup(get_game_log_main.content, "html.parser")

     #  get player years
        for line in career_soup.find_all('div', id='game-log-year'):
            for option in line.find_all('option'):
               option = str(option)
               split_one = option.split('<')
               split_one = str(split_one[1])
               split_two = split_one.split('>')
               final_year = str(split_two[1])
               year_array.append(final_year)
        player_years[key] = year_array
        year_array = []
    #return year_array
    print('All player years found...')
    return player_years

#TODO: Move this to new game to game util if necessary
def create_extended_link(link_dict, year_dict):
    print('Finalizing data structure... ')
    key_array = []
    position_array = []
    career_link_array = []
    player_game_log_dict = {}
    player_situational_dict = {}
    full_game_log = []
    full_situational = []
    final_dictionary = {}
    key_num = 0

    #deconstruct the dictionary passed in
    for key, value in link_dict.items():
        player_game_log_dict[key] = value[2]
        key_array.append(key)
        position_array.append(value[0])
        career_link_array.append(value[1])

    for key, value in link_dict.items():
        player_situational_dict[key] = value[3]

    #make full game log array of links
    for (pgkey, pgvalue), (ydkey, ydvalue) in zip(player_game_log_dict.items(), year_dict.items()):
        if(pgkey == ydkey):
            game_log_array = []

            for year in ydvalue:
                string_year = str(year)
                string_link = str(pgvalue)
                full_link = string_link + '?season=' + string_year
                game_log_array.append(full_link)
        full_game_log.append(game_log_array)

    #make full situational array of links
    for (sitkey, sitvalue), (ydkey, ydvalue) in zip(player_situational_dict.items(), year_dict.items()):
        if (sitkey == ydkey):
            situational_array = []

            for year in ydvalue:
                string_year = str(year)
                string_link = str(sitvalue)
                full_link = string_link + '?season=' + string_year
                situational_array.append(full_link)
        full_situational.append(situational_array)

    #make final link dictionary
    for key in key_array:
        full_array = []
        full_array.append(position_array[key_num])
        full_array.append(full_game_log[key_num])
        full_array.append(full_situational[key_num])
        full_array.append(career_link_array[key_num])
        final_dictionary[key] = full_array
        key_num += 1
    print('Final data structure complete...')
    return(final_dictionary)

#TODO: ADD SQL CALLS
def career_stats_table_parse(updated_player_link_dict):
    for key, value in updated_player_link_dict.items():
        get_career_data = requests.get(value[3])
        career_soup = BeautifulSoup(get_career_data.content, "html.parser")
        name = str(key).split(',')
        passing_string = 'Career Stats In Passing For' + name[1] + ' ' +name[0]
        rushing_string = 'Career Stats In Rushing For' + name[1] + ' ' +name[0]
        receiving_string = 'Career Stats In Receiving For' + name[1] + ' ' +name[0]
        defensive_string = 'Career Stats In Defensive For' + name[1] + ' ' +name[0]
        kick_return_string = 'Career Stats In Kick Return For' + name[1] + ' ' +name[0]
        punt_return_string = 'Career Stats In Punt Return For' + name[1] + ' ' +name[0]
        punt_string = 'Career Stats In Punting Stats For' + name[1] + ' ' +name[0]
        kickoff_string = 'Career Stats In Kickoff Stats For' + name[1] + ' ' +name[0]
        index_counter=0
        table_counter=0
        skip_function=0
        table_array=[]

        if(value[0] == 'QB'):
            table_array = [passing_string, rushing_string]
        if (value[0] == 'RB') or (value[0] == 'WR') or (value[0] == 'TE'):
            table_array = [rushing_string, receiving_string, kick_return_string, punt_return_string]
        if (value[0] == 'CB') or (value[0] == 'LB') or (value[0] == 'MLB') or (value[0] == 'DB') or (value[0] == 'DE') or (value[0] == 'FS') or (value[0] == 'OLB'):
            table_array = [defensive_string]
        if (value[0] == 'K') or (value[0] == 'P'):
            table_array = [kickoff_string, punt_string]

        for table in table_array:
            table = career_soup.find('table', summary=table_array[table_counter])
            try:
                table_row = table.find_all('tr')
            except:
                print("Cannot parse table: " + key)
                skip_function = 1
            if(not skip_function):
                for line in table_row[0:len(table_row)]:
                    row = str(table_row[index_counter])
                    split = row.split('>')
                    #TODO: THIS IS WHERE THE SQL CALLS WILL GO


                    print(str(index_counter) + str(key) + str(split))
                    index_counter+=1
                index_counter = 0

            table_counter += 1
        #table_counter = 0

#TODO: GET SECOND TABLE
#TODO: ADD SQL CALLS
def game_logs_table_parse(updated_player_link_dict):
    table_counter = 0
    for (key, value) in updated_player_link_dict.items():
        name = str(key).split(',')
        #print(name)
        for each_link in value[1]:
            year = str(each_link).split('=')
            game_log_string = 'Game Logs For' + name[1] + ' ' + name[0] + ' ' + 'In ' +  year[1]
            get_game_log_data = requests.get(each_link)
            career_soup = BeautifulSoup(get_game_log_data.content, "html.parser")

            index_counter = 0
            skip_function = 0

            table = career_soup.find('table', summary=game_log_string)
            try:
                table_row = table.find_all('tr')
            except:
                print("Cannot parse table: " + key)
                skip_function = 1
            if (not skip_function):
                row = str(table_row[index_counter])
                split = row.split('>')
                # TODO: THIS IS WHERE THE SQL CALLS WILL GO

                print(str(index_counter) + str(key) + str(split))
                index_counter += 1
            print(table_counter)
        table_counter = 0
    table_counter = 0

#TODO: ADD SQL CALLS
def situational_stats_parse(updated_player_link_dict):
    for (key, value) in updated_player_link_dict.items():
        name = str(key).split(',')
        #print(name)
        for each_link in value[2]:
            by_attempts = 'Stats By Attempts For' + name[1] + ' ' + name[0]
            by_field_posiiton = 'Stats By Field Position For' + name[1] + ' ' + name[0]
            by_half = 'Stats By Half For' + name[1] + ' ' + name[0]
            by_point_situation = 'Stats By Point Situation For' + name[1] + ' ' + name[0]
            by_quarters = 'Stats By Quarters' + name[1] + ' ' + name[0]
            by_home_away = 'Stats By Home/Away' + name[1] + ' ' + name[0]
            by_margin = 'Stats By Margin' + name[1] + ' ' + name[0]
            by_field_type = 'Stats By Field Type' + name[1] + ' ' + name[0]
            table_array = [by_attempts, by_field_posiiton, by_half, by_point_situation, by_quarters, by_home_away, by_margin, by_field_type]

            get_game_log_data = requests.get(each_link)
            career_soup = BeautifulSoup(get_game_log_data.content, "html.parser")

            index_counter = 0
            table_counter = 0
            skip_function = 0

            for table in table_array:
                table = career_soup.find('table', summary=table_array[table_counter])
                try:
                    table_row = table.find_all('tr')
                except:
                    print("Cannot parse table " + table_array[table_counter])
                    skip_function = 1
                if (not skip_function):
                    for line in table_row[0:len(table_row)]:
                        row = str(table_row[index_counter])
                        split = row.split('>')
                        # TODO: THIS IS WHERE THE SQL CALLS WILL GO
                        # TODO: NEED TO ADD HOOK FOR OFFENSIVE/DEFENSIVE/KP POSITIONS
                        print(str(index_counter) + str(key) + str(split))
                        index_counter += 1
                    index_counter = 0

                table_counter += 1
            # table_counter = 0