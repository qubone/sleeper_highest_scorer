import json
from typing import List
import requests
import argparse

from script.players.players import get_all_players
from script.common.common import (
    http_get_response_data_json,
    write_json_to_file
    )

LEAGUE_ID = '872554216374337536'
TEST_LEAGUE = 'https://api.sleeper.app/v1/league/872554216374337536/'
MATCHUP = 'https://api.sleeper.app/v1/league/<league_id>/matchups/<week>'
SLEEPER_API = "https://docs.sleeper.com/"

class LeagueData:
    def __init__(self, league_id: str) -> None:
        self.base_url = "https://api.sleeper.app/v1/league/"
        self.league_id = league_id
        self.league_url = self.base_url + self.league_id
        self.league_users: List[str] = list()
        self.week = ""

    def get_league_url(self):
        return self.league_url
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
        
class MatchUpData:
    def __init__(self, matchup_data) -> None:
        self.starter_points = matchup_data["starters_points"]
        self.starters = matchup_data["starters"]
        self.roster_id = matchup_data["roster_id"]
        self.points = matchup_data["points"]
        self.player_points = matchup_data["players_points"]
        self.players = matchup_data["players"]
        self.matchup_id = matchup_data["matchup_id"]
        self.custom_points = None
    def get_starter_points(self):
        return self.starter_points
    def get_starters(self):
        return self.starters
    def get_roster_id(self):
        return self.roster_id
    def get_points(self):
        return self.points
    def get_player_points(self):
        return self.player_points
    def get_players(self):
        return self.players
    def get_matchup_id(self):
        return self.matchup_id
    def get_custom_points(self):
        return self.custom_points

class MatchUp:
    def __init__(self, a, week) -> None:
        #self.matchup_url = league_url + '/matchups/' + week
        self.weekly_matchups = self.get_matchup_data()
        self.test = ""
        
    def get_weekly_matchups(self):
        data = requests.get(self.matchup_url)
        return data.text
    def get_matchup_data(self) -> List[MatchUpData]:
        data = requests.get(self.matchup_url)
        json_text = json.loads(data.text)
        match_up_data = list()
        for item in json_text:
            match_up_data.append(MatchUpData(item))
        return match_up_data
    
    def get_highest_scorer(self):
        #prints highest score
        highest_score = 0.0
        highest_scorer: MatchUp = None
        first_score = self.get_matchup_data()[0]
        for matchup in self.get_matchup_data():
            first_score = matchup.get_player_points()
            score = matchup.get_points()
            print("reading score: ", score)
            if  score > highest_score:
                highest_score = score
                highest_scorer = matchup
        print("highest score: ", highest_score)

        #todo: add all total points to a list and sort them (name, points)

def get_call():
    league = LeagueData(LEAGUE_ID)
    league_matchups = http_get_response_data_json(TEST_LEAGUE + '/matchups/' + '2')
    test_week = '2'
    base_url = league.get_league_url()
    matchup = MatchUp(base_url, test_week)
    test = matchup.get_weekly_matchups()
    matchups = matchup.get_matchup_data()
    
    print(matchup.get_highest_scorer())


def main(database: str):
    ''' Entry point. '''
    get_all_players(database)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', '-database', help='Player database output')
    args = parser.parse_args()
