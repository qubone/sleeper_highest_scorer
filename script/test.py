from sleeperpy import Players
import json
#from script.common.common import http_get_response_data_json, write_json_to_file
#from script.common.common import write_json_to_file
players = Players()
player_data = players.get_all_players()
output_file = "C:/Users/Linus\Desktop/Programming/sleeper_highest_scorer/script/resources/players_db.json"

with open(output_file, "w") as out:
    json.dump(player_data, out, indent=4)

#write_json_to_file(player_data, output_file)