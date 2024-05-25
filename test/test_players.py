import pytest
from script.players.players import Player

class Setup:
    def __init__(self) -> None:
        self.player_id = '00000000'
        self.database = "C:/Users/Linus\Desktop/Programming/sleeper_highest_scorer/script/resources/players_db.json"

@pytest.fixture()
def setup():
    return Setup
