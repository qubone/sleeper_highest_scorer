from pathlib import Path
from pytest import MonkeyPatch, fixture
from script.api_parser import SleeperAPIParser
import requests

from unittest.mock import MagicMock, Mock
from script.players.players import Player
from script.leagues.leagues import League
from script.drafts import Draft
from typing import List



class Setup:
    ''' Setup class for shared test input data. '''
    def __init__(self) -> None:
        self.user_name = 'Linusbo'
        self.user_id = '727977584134025216'
        self.league_id = '1004113252818726912'
        self.season = '2023'
        self.avatar = '88700289dc890fc9064fb95f84b1c3eb'
        self.test_url = 'https://api.sleeper.app/v1/user/727977584134025216/leagues/nfl/2023'
        self.database = "script/resources/players_db.json"

        self.test_user_data = {
                    "username": "linusbo",
                    "user_id": "727977584134025216",
                    "is_bot": False,
                    "display_name": "Linusbo",
                    "avatar": "88700289dc890fc9064fb95f84b1c3eb"}
        self.mocker = MagicMock()
        self.api_parser = SleeperAPIParser()
        
        #TODO: MonkeyPatch

@fixture(name="setup")
def setup_fixture():
    ''' Pytest decorator to use shared Setup class for testing. '''
    return Setup()


def test_get_players(setup: Setup, monkeypatch: MonkeyPatch):
    #get_user_call = SleeperAPIParser().get_user(setup.user_id)
    #http_get = SleeperAPIParser()._http_get_response_data_json(setup.test_url)

    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.text = '{ \
                    "username":"linusbo", \
                    "user_id":"727977584134025216", \
                    "is_bot":false, \
                    "display_name":"Linusbo", \
                    "avatar":"88700289dc890fc9064fb95f84b1c3eb"}'
                self.ok = True
                self.status = 200
        response = MockResponse()
    monkeypatch.setattr(SleeperAPIParser()._http_get_response_data_json(setup.test_url), "get", mock_get)
    
    result, ok, status = SleeperAPIParser().get_user(setup.user_id)
    assert result == '{ \
                     "username":"linusbo", \
                     "user_id":"727977584134025216", \
                     "is_bot":false, \
                     "display_name":"Linusbo", \
                     "avatar":"88700289dc890fc9064fb95f84b1c3eb"}'
    assert ok is True
    assert status == 200


def test_get_players_using_mock(setup: Setup):
    fake_resp = Mock()
    #fake_resp.json = setup.mocker(return_value=setup.test_user_data)
    #fake.re


def contains_letter(s: str):
    return any(char.isalpha() for char in s)


def test_get_all_drafts_for_user(setup: Setup):
    response = setup.api_parser.get_all_drafts_for_user(setup.user_id, "2024")
    for draft in response:
        test = Draft(draft)
        print(test)
    pass


def test_get_trending_players(setup: Setup):
    """Get trending players and check if rostered in any league.

    Args:
        setup (Setup): _description_
    """
    response = setup.api_parser.get_trending_players(trend_type="add", lookback_hours="24", limit="25")
    trending_up_players = []
    for trend in response:
        player = trend['player_id']
        #TODO: Add filter for SF
        if not contains_letter(player):
            # Keep player as id for performance
            #players.append(Player(player))
            trending_up_players.append(player)

            #if player.position = "position": "K",
            #pass
            # Kicker
        else:
            defense = Player(player)
            print("TEST")
    #print(trending_up_players)

    #Get all leagues of user
    leagues = setup.api_parser.get_all_leagues_for_user(setup.user_id)
    league_list: List[League] = []
    # Create league objects for each league
    for league in leagues:
        league_list.append(League.from_dict(league))
    rostered_players = []
    available_players = []
    # Loop through all leagues
    for li in league_list:
        #test = li.rosters
        # Loop through all rosters in a league
        rosters = li.rosters
        for roster in rosters:
            roster_players = roster["players"]
            rostered_players.extend(roster_players)
        #print("Test")
        for player in trending_up_players:
            if player not in rostered_players:
                available_players.append(Player(player))
        # Find all players in a roster
        print("\nAvailable players in ", li)
        print(available_players)
        print("############")
    print("Test")

    # Get all rosters in a league
    # Should be inside League class
    rosters = setup.api_parser.get_rosters_in_a_league()
    # Check if each player are on any roster in a league
    # Loop through rosters


    


'''
def test(setup: Setup, monkeypatch: MonkeyPatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
        def __init__(self):
            self.text = '{"username":"linusbo","user_id":"727977584134025216","is_bot":false,"display_name":"Linusbo","avatar":"88700289dc890fc9064fb95f84b1c3eb"}'
            self.ok = True
            self.status = 200
        response = MockResponse()
        return response
    
    monkeypatch.setattr(requests, "get", mock_get)
    result, ok, status_code = get_players()
    assert result == "<a href.......'
    assert ok is True
    assert status_code = 200

    
    
    
    
from unittest.mock import MagickMock

mock_download = MagicMock(return_value='path/to/file.zip')
mock_unpack = MagicMock()

monkeypatch.setattr('SleeperAPIParser().get_players(), 'mock_download')

)
    
    
    
    '''