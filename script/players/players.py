"""All data related to players."""
from typing import Dict, List, Any
from script.common.common import read_json_from_file
from dataclasses import dataclass
from enum import Enum

class PlayerPersonal:
    ''' Class for personal player data. '''
    def __init__(self,  player_db: Dict[str, Any]) -> None:
        self.full_name = player_db['full_name']
        self.age = player_db['age']
        self.weight = player_db['weight']
        self.height = player_db['height']
        self.birth_date = player_db['birth_date']
        self.college = player_db['college']
        self.high_school = player_db['high_school']

class PlayerPersonal:
    """Class for personal player data."""
    def __init__(self,  player: Dict[str, Any]) -> None:
        self._full_name: str = player.get('full_name')
        self._age: int = player.get('age')
        self._weight: str = player.get('weight')
        self._height: str = player.get('height')
        self._birth_date: str = player.get('birth_date')
        self._college: str = player.get('college')
        self._high_school: str = player.get('high_school')

    @property
    def full_name(self) -> str:
        """Full name of the player."""
        return self._full_name

    @property
    def age(self) -> int:
        """Age of the player."""
        return self._age

    @property
    def weight(self) -> str:
        """Weight (lbs) of the player."""
        return self._weight

    @property
    def height(self) -> str:
        """Height (ft) of the player."""
        return self._height

    @property
    def birth_date(self) -> str:
        """Birthday of the player."""
        return self._birth_date

    @property
    def college(self) -> str:
        """Returns the last college of the player."""
        return self._college

    @property
    def high_scool(self) -> str:
        """High school of the player."""
        return self._high_school

    def get_first_name(self) -> str:
        ''' Returns the last name of the player. '''
        return str(self.full_name.split(" "))[0]

    def get_last_name(self) -> str:
        ''' Returns the first name of the player. '''
        return str(self.full_name.split(" "))[1]


class Position(Enum):
    QB = "QB"
    WR = "WR"
    RB = "RB"
    TE = "TE"
    K = "K"

class Status(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

class Team(Enum):
    KANSAS_CITY = 'KC'
    ARIZONA = 'ARI'




class PlayerProfessional:
    """Class for professional player data."""
    def __init__(self,  player: Dict[str, Any]) -> None:
        self._years_exp: int = player.get('years_exp')
        self._team: Team = player.get('team')
        self._number: int = player.get('number')
        self._position: Position = player.get('position')
        self._status: Status = player.get('status')
        self._depth_chart_order: int = player.get('depth_chart_order')

    @property
    def years_exp(self) -> int:
        """Number of years experience of the player."""
        return self._years_exp

    @property
    def team(self) -> Team:
        """Current team of the player."""
        return self._team

    @property
    def number(self) -> int:
        """Current jersey number of the player."""
        return self._number

    @property
    def position(self) -> Position:
        """Position of the player."""
        return self._position

    @property
    def status(self) -> Status:
        """Status of the player."""
        return self._status

    @property
    def depth_chart_order(self) -> int:
        """Current depth chart order of the player."""
        return self._depth_chart_order


class PlayerSleeper:
    """Class for player data related to Sleeper.""" 
    def __init__(self,  player: Dict[str, Any]) -> None:
        self._player_id: str = player.get('player_id')
        self._metadata: Dict[str, str] = player.get('metadata')
        self._fantasy_positions: List[Position] = player['fantasy_positions']

    @property
    def player_id(self) -> str:
        """Sleeper ID of the player."""
        return self.player_id

    @property
    def metadata(self) -> Dict[str, str]:
        """Sleeper metadata of the player."""
        return self.metadata

    @property
    def fantasy_positions(self) -> List[Position]:
        """Sleeper fantasy positions of the player."""
        return self.fantasy_positions

@dataclass
class PlayerDB:
    player_db: str = "script/resources/players_db.json"
    

class Player:
    ''' Constructs player data based on the player ID. '''
    def __init__(self, player_id: str) -> None:
        self._id = player_id
        self.player_db = PlayerDB
        db = read_json_from_file(self.player_db.player_db)
        if self._id in db:
            found_player = db.get(self.id)
            self._personal = PlayerPersonal(found_player)
            self._professional = PlayerProfessional(found_player)
            self._sleeper_data = PlayerSleeper(found_player)


    @property
    def id(self) -> str:
        """Sleeper ID of the Player."""
        return self._id

    @property
    def personal(self) -> PlayerPersonal:
        """Personal data of the Player."""
        return self._personal

    @property
    def professional(self) -> PlayerProfessional:
        """Professional data of the Player."""
        return self._professional

    @property
    def sleeper(self) -> PlayerProfessional:
        """Sleeper data of the Player."""
        return self._sleeper_data

