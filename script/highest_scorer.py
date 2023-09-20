import requests
import argparse
import json
from typing import List

LEAGUE_ID = '872554216374337536'
TEST_LEAGUE = 'https://api.sleeper.app/v1/league/872554216374337536/'
MATCHUP = 'https://api.sleeper.app/v1/league/<league_id>/matchups/<week>'
SLEEPER_API = "https://docs.sleeper.com/"

class User:
    def __init__(self, user_data) -> None:
        self.user_id = user_data["user_id"]
        self.settings = user_data["settings"]
        self.metadata = None
        self.league_id = user_data["league_id"]
        self.is_owner = user_data["is_owner"]
        self.is_bot = user_data["is_bot"]
        self.display_name = user_data["display_name"]
        self.avatar = None
    def get_user_id(self) -> str:
        return self.user_id
    def get_settings(self):
        return self.settings
    def get_metadata(self):
        return None
    def get_league_id(self) -> str:
        return self.league_id
    def get_is_owner(self):
        return self.is_owner
    def get_is_bot(self) -> bool:
        return self.is_bot
    def get_display_name(self) -> str:
        return self.display_name
    def get_avatar(self):
        return None

class LeagueData:
    def __init__(self, league_id: str) -> None:
        self.base_url = "https://api.sleeper.app/v1/league/"
        self.league_id = league_id
        self.league_url = self.base_url + self.league_id
        self.league_users: List[str] = list()
        self.week = ""

    def get_league_id(self):
        return self.league_id
    def get_league_users(self) -> List[User]:
        league_users = requests.get(f'{self.league_url}/users')
        list_of_users =  json.loads(league_users.text)
        league_users: List[User] = list()
        for user_data in list_of_users:
            user = User(user_data)
            league_users.append(user)
        return league_users
    def get_week(self):
        return self.week
        

def http_get_call(url: str):
     return requests.get(url)



def get_total_points():
    pass


def get_call():
    league_users = requests.get('https://api.sleeper.app/v1/league/872554216374337536/users')
    league_matchups = http_get_call(TEST_LEAGUE + '/matchups/' + '2')
    text = league_matchups.text
    users_txt = json.loads(league_users.text)
    json_text = json.loads(text)
    league = LeagueData(LEAGUE_ID)
    users = league.get_league_users()

    for user in users:
        user_id = user.get_user_id()
        print(user_id)

    matchups = list()
    for matchup in json_text:
        matchups.append(matchup)
        res = matchup["points"]

    print(league_users.text)

def main():
    get_call()