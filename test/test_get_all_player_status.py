from pathlib import Path
from typing import List
import pytest

from script.common import write_json_to_file, read_json_from_file
from script.user import User
from script.model.avatar import Avatar
from script.leagues.rosters import (Roster,
                                    Metadata, Settings,
                                    WaiverData, TotalPoints,
                                    Players)
from script.leagues.leagues import League, LeagueParse
from script.players.players import Player
from script.get_all_player_status import Parser, SleeperAPIParser

class Setup:
    ''' Setup class for shared test input data. '''
    def __init__(self) -> None:
        self.user_id = '727977584134025216'
        self.database = "script/resources/players_db.json"
        self.parser = SleeperAPIParser()


@pytest.fixture(name="setup")
def setup_fixture():
    """Pytest decorator to use shared Setup class for testing."""
    return Setup()

def test_parser(setup: Setup):
    test = Parser(setup.user_id)
    user_leagues: List[League] = test.leagues
    #user_league_ids = [x.league_id for x in user_leagues]
    #print(user_leagues)
    #print(user_league_ids)

    for id in user_leagues:
        rosters = setup.parser.get_rosters_in_a_league(id.league_id)
        for roster in rosters:
            test2 = Roster.from_dict(roster)
            unique_players = []
            starters = test2.starters
            for starter in starters:
                if starter not in unique_players:
                    unique_players.append(starter)
                starter.player.professional.injury.status
            print(starters)