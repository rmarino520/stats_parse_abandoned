import requests
import nfl_utils as nu
import re
import time
from bs4 import BeautifulSoup
import mysql.connector

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="XXXXX",
  database = 'ffstats'
)

#print(mydb)

mycursor = mydb.cursor()

#Prompt for input
#if team == "49ers":
#    team = "fourtyniners"


team_array = ['bengals', 'bills', 'broncos', 'browns', 'buccaneers', 'cardinals', 'chargers', 'chiefs', 'colts',\
              'cowboys', 'dolphins', 'eagles', 'falcons', 'fortyniners', 'giants', 'jaguars', 'jets', 'lions', 'packers',\
              'panthers', 'patriots', 'raiders', 'rams', 'ravens', 'redskins', 'saints', 'seahawks', 'steelers', 'texans', \
               'titans', 'vikings']



# name = 'This is a test'
# for test_team in team_array:
#     mycursor.execute("INSERT INTO team_names (team_name) VALUES ('%s')" %(test_team))
# mydb.commit()

# mycursor.execute("insert into player_names set team_name = '%s', player_name = '%s', player_position = '%s', \
# team_id = (select team_id from team_names where team_name = '%s'); " \
#                  % (team_array[team_number], str(key), value[0], team_array[team_number]))
# mydb.commit()

team_number = 0
for team in team_array:
    #position = 'QB'
    "Make the URL"
    main_url = nu.make_team_url(team_array[team_number])
   #print(main_url)

#Open URL
    r = requests.get(main_url)
    main_soup = BeautifulSoup(r.content, "html.parser")

#make player link dictionary
    simple_player_link_dict = nu.process_player_link(main_soup)

#store years in league in dictionary
#for accessing game to game logs and situational stats
    year_dict = nu.process_years_in_league(simple_player_link_dict)

#update game logs and situational stats with year
    updated_player_link_dict = nu.create_extended_link(simple_player_link_dict, year_dict)

    #nu.career_stats_table_parse(updated_player_link_dict)
    #nu.situational_stats_parse(updated_player_link_dict)
    nu.game_logs_table_parse(updated_player_link_dict)




    #team_number+=1


