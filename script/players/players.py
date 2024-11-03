"""All data related to players."""
from typing import Dict, List, Any, Optional
from script.common import read_json_from_file
from script.constants import InjuryStatus, InjuryNotes, InjuryBodyPart, Status, NFLPosition
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from script.api_parser import SleeperAPIParser


@dataclass
class BirthData:
    """Birth data of a player.
    """
    birth_date: str
    birth_state: Optional[str]
    birth_country: Optional[str]
    birth_city: Optional[str]


@dataclass
class BodyMeasures:
    """Body measures of a player.
    """
    weight: str
    height: str


@dataclass
class Names:
    """Names of a player.
    """
    full_name: str
    first_name: str
    last_name: str

@dataclass
class Education:
    """Educational institutes of a player.
    """
    high_school: Optional[str]
    college: Optional[str]


class Personal:
    """Class for personal player data.
    """
    def __init__(
        self,
        full_name: str,
        age: int,
        weight: str,
        height: str,
        birth_date: str,
        college: Optional[str],
        high_school: Optional[str],
        birth_state: Optional[str],
        birth_country: Optional[str],
        birth_city: Optional[str],
        first_name: str,
        last_name: str
    ) -> None:
        self._names = Names(full_name, first_name, last_name)
        self._body_measures = BodyMeasures(weight, height)
        self._birth_data = BirthData(
            birth_date, birth_state, birth_country, birth_city)
        self._education = Education(high_school, college)
        self._age = age

    @property
    def names(self) -> Names:
        """Full name of the player.
        """
        return self._names

    @property
    def body_measures(self) -> BodyMeasures:
        """Weight (lbs) and height (ft) of the player.
        """
        return self._body_measures

    @property
    def birth_data(self) -> BirthData:
        """Birth data of the player.
        """
        return self._birth_data

    @property
    def education(self) -> Education:
        """Returns the educational institues of a player.
        High school and college.

        Players that joined through international programs
        might not have played in college.
        """
        return self._education

    @property
    def age(self) -> int:
        """Age of the player.
        """
        return self._age


class Injury:
    """Injury data.

    Returns:
        _type_: _description_
    """
    def __init__(
        self,
        injury_status: Optional[InjuryStatus],
        injury_start_date: Optional[str],
        injury_notes: Optional[InjuryNotes],
        injury_body_part: Optional[InjuryBodyPart],
    ) -> None:
        self._status = injury_status
        self._start_date = injury_start_date
        self._notes = injury_notes
        self._body_part = injury_body_part
    
    @property
    def status(self) -> Optional[InjuryStatus]:
        """Injury status of the player.
        """
        return self._status


class MetaData:
    """Class for player metadata.
    """
    def __init__(
        self,
        rookie_year: Optional[str],
        injury_override_regular_2020_5: Optional[str],
        override_active: Optional[str],
        years_exp_shift: Optional[str],
        source_id: Optional[str],
        name: Optional[str]
    ) -> None:
        self._rookie_year = rookie_year
        self._injury_override_regular_2020_5 = injury_override_regular_2020_5
        self._override_active = override_active
        self._years_exp_shift = years_exp_shift
        self._source_id = source_id
        self._name = name
   
    @property
    def rookie_year(self) -> Optional[str]:
        """Rookie year of a player.
        """
        return self._rookie_year

    @classmethod
    def from_dict(cls, meta_data: Dict[str, Any]):
        """Creates User object from dictionary data.

        Args:
            meta_data (Dict[str, Any]): metadata from players database
        """
        return cls(
            rookie_year=meta_data.get("rookie_year"),
            injury_override_regular_2020_5=meta_data.get(
                "injury_override_regular_2020_5"
            ),
            override_active=meta_data.get("override_active"),
            years_exp_shift=meta_data.get("years_exp_shift"),
            source_id=meta_data.get("source_id"),
            name=meta_data.get("name"),
        )


class Professional:
    """Class for professional player data."""
    def __init__(
        self,
        years_exp: Optional[int],
        team: Optional[str],
        number: Optional[int],
        position: Optional[str],
        status: Optional[str],
        depth_chart_order: Optional[int],
        depth_chart_position: Optional[Any],
        active: bool,
        sport: str,
        injury: Optional[Injury]
    ) -> None:
        self._years_exp = years_exp
        self._team = team
        self._number = number
        self._position = NFLPosition(position)
        self._status = Status(status)
        self._depth_chart_order = depth_chart_order
        self._depth_chart_position = depth_chart_position
        self._active = active
        self._sport = sport
        self._injury = injury

    @property
    def years_exp(self) -> Optional[int]:
        """Number of years experience of the player."""
        return self._years_exp

    @property
    def team(self) -> Optional[str]:
        """Current team of the player."""
        return self._team

    @property
    def number(self) -> Optional[int]:
        """Current jersey number of the player."""
        return self._number

    @property
    def position(self) -> NFLPosition:
        """Position of the player."""
        return self._position

    @property
    def status(self) -> Status:
        """Status of the player."""
        return self._status

    @property
    def depth_chart_order(self) -> Optional[int]:
        """Current depth chart order of the player."""
        return self._depth_chart_order
    
    @property
    def injury(self) -> Optional[Injury]:
        """Injury information of the player.
        """
        return self._injury


class Sleeper:
    """Class for player data related to Sleeper."""

    def __init__(
        self,
        player_id: str,
        fantasy_positions: Optional[List[str]],
        metadata: Optional[Dict[str, Any]],
        fantasy_data_id: Optional[int],
        stats_id: Optional[int],
        hashtag: str,
        search_rank: Optional[int],
        search_first_name: str,
        search_last_name: str,
        search_full_name: str,
        news_updated: Optional[int],
    ) -> None:
        self._player_id = player_id
        self._fantasy_positions = fantasy_positions
        self._metadata = metadata
        self._fantasy_data_id = fantasy_data_id
        self._stats_id = stats_id
        self._hashtag = hashtag
        self._search_rank = search_rank
        self._search_first_name = search_first_name
        self._search_last_name = search_last_name
        self._search_full_name = search_full_name
        self._news_updated = news_updated

    @property
    def player_id(self) -> str:
        """Sleeper ID of the player."""
        return self._player_id

    @property
    def fantasy_positions(self) -> Optional[List[str]]:
        """Sleeper fantasy positions of the player."""
        return self.fantasy_positions

    @property
    def metadata(self) -> Dict[str, str]:
        """Sleeper metadata of the player."""
        return self.metadata


class ThirdPartyPlatformData:
    """Third-party platform data.
    ESPN
    Rotoworld
    Rotowire
    Oddsjam
    Pandascore
    GSIS
    SWISH
    Sportsradar
    """
    def __init__(
        self,
        espn_id: int,
        rotoworld_id: int,
        rotowire_id: int,
        oddsjam_id: Optional[Any],
        pandascore_id: Optional[Any],
        gsis_id: str,
        swish_id: Optional[Any],
        sportsradar_id: str,
        yahoo_id: int
    ) -> None:
        self._espn_id = espn_id
        self._rotoworld_id = rotoworld_id
        self._rotowire_id = rotowire_id
        self._oddsjam_id = oddsjam_id
        self._pandascore_id = pandascore_id
        self._gsis_id = gsis_id
        self._swish_id = swish_id
        self._sportradar_id = sportsradar_id
        self._yahoo_id = yahoo_id


@dataclass
class PlayerDB:
    player_db: str = "script/resources/players_db.json"


class DefensePlayerModel:
    """Defense model parsed from JSON.
    """
    def __init__(
        self,
        active: bool,
        position: str,
        sport: str,
        player_id: str,
        fantasy_positions: List[str],
        last_name: str,
        first_name: str,
        team: str,
        injury_status: Optional[str] = None
    ) -> None:
        self._active = active,
        self._position = position,
        self._sport = sport,
        self._player_id = player_id,
        self._fantasy_positions = fantasy_positions,
        self._last_name = last_name,
        self._first_name = first_name,
        self._team = team,
        self._injury_status = injury_status,

    @classmethod
    def from_dict(cls, player_data: Dict[str, Any]):
        """Creates User object from dictionary data.

        Args:
            user_data (Dict[str, Any]): _description_

        Returns:
            _type_: _description_
        """
        return cls(
            active = player_data["active"],
            position = player_data["position"],
            sport = player_data["sport"],
            player_id = player_data["player_id"],
            fantasy_positions = player_data["fantasy_positions"],
            last_name = player_data["last_name"],
            first_name = player_data["first_name"],
            team = player_data["team"],
            injury_status = player_data["injury_status"]
        )
class PlayerFullModel:
    """A full model parsed from JSON.
    """
    # pylint: disable=R0902, R0913, R0914
    def __init__(
        self,
        birth_state: Optional[str],
        practice_description: Optional[str],
        depth_chart_position: Optional[Any],
        fantasy_positions: List[str],
        years_exp: int,
        yahoo_id: int,
        full_name: str,
        weight: str,
        position: str,
        injury_notes: Optional[InjuryNotes],
        dl_trading_id: Optional[Any],
        first_name: str,
        injury_body_part: Optional[InjuryBodyPart],
        search_full_name: str,
        depth_chart_order: Optional[Any],
        last_name: str,
        injury_start_date: Optional[str],
        birth_country: str,
        practice_participation: Optional[Any],
        birth_date: str,
        height: str,
        espn_id: int,
        search_rank: int,
        status: str,
        sportradar_id: str,
        oddsjam_id: Optional[Any],
        injury_status: Optional[InjuryStatus],
        player_id: str,
        high_school: str,
        news_updated: int,
        swish_id: Optional[Any],
        stats_id: int,
        fantasy_data_id: int,
        search_first_name: str,
        metadata: Dict[str, Any],
        sport: str,
        active: bool,
        rotowire_id: int,
        search_last_name: str,
        hashtag: str,
        pandascore_id: Optional[Any],
        team: str,
        birth_city: str,
        college: str,
        gsis_id: str,
        rotoworld_id: int,
        number: int,
        age: int,
    ) -> None:
        self._personal = Personal(
            full_name,
            age,
            weight,
            height,
            birth_date,
            college,
            high_school,
            birth_state,
            birth_country,
            birth_city,
            first_name,
            last_name
        )
        self._professional = Professional(
            years_exp,
            team,
            number,
            position,
            status,
            depth_chart_order,
            depth_chart_position,
            active,
            sport,
            injury=Injury(
                injury_status,
                injury_start_date,
                injury_notes,
                injury_body_part
            ),
        )
        self._third_party = ThirdPartyPlatformData(
            espn_id,
            rotoworld_id,
            rotowire_id,
            oddsjam_id,
            pandascore_id,
            gsis_id,
            swish_id,
            sportradar_id,
            yahoo_id,
        )
        self._sleeper = Sleeper(
            player_id,
            fantasy_positions,
            metadata,
            fantasy_data_id,
            stats_id,
            hashtag,
            search_rank,
            search_first_name,
            search_last_name,
            search_full_name,
            news_updated
        )


    @property
    def personal(self) -> Personal:
        """Personal data of the player."""
        return self._personal

    @property
    def professional(self) -> Professional:
        """Professional data of the player."""
        return self._professional

    @property
    def third_party(self) -> ThirdPartyPlatformData:
        """Third-party platform data of the player."""
        return self._third_party

    @property
    def sleeper(self) -> Sleeper:
        """Sleeper data of the player."""
        return self._sleeper

    @classmethod
    def from_dict(cls, player_data: Dict[str, Any]):
        """Creates User object from dictionary data.

        Args:
            user_data (Dict[str, Any]): _description_

        Returns:
            _type_: _description_
        """
        return cls(
            birth_state=player_data.get("birth_state", ""),
            practice_description=player_data["practice_description"],
            depth_chart_position=player_data["depth_chart_position"],
            fantasy_positions=player_data["fantasy_positions"],
            years_exp=player_data["years_exp"],
            yahoo_id=player_data["yahoo_id"],
            full_name=player_data["full_name"],
            weight=player_data["weight"],
            position=player_data["position"],
            injury_notes=player_data["injury_notes"],
            dl_trading_id=player_data.get("dl_trading_id"),
            first_name=player_data["first_name"],
            injury_body_part=player_data["injury_body_part"],
            search_full_name=player_data["search_full_name"],
            depth_chart_order=player_data["depth_chart_order"],
            last_name=player_data["last_name"],
            injury_start_date=player_data["injury_start_date"],
            birth_country=player_data["birth_country"],
            practice_participation=player_data["practice_participation"],
            birth_date=player_data["birth_date"],
            height=player_data["height"],
            espn_id=player_data["espn_id"],
            search_rank=player_data["search_rank"],
            status=player_data["status"],
            sportradar_id=player_data["sportradar_id"],
            oddsjam_id=player_data["oddsjam_id"],
            injury_status=player_data["injury_status"],
            player_id=player_data["birth_state"],
            high_school=player_data["high_school"],
            news_updated=player_data["news_updated"],
            swish_id=player_data["swish_id"],
            stats_id=player_data["stats_id"],
            fantasy_data_id=player_data["fantasy_data_id"],
            search_first_name=player_data["search_first_name"],
            metadata=player_data["metadata"],
            sport=player_data["sport"],
            active=player_data["active"],
            rotowire_id=player_data["rotowire_id"],
            search_last_name=player_data["search_last_name"],
            hashtag=player_data["hashtag"],
            pandascore_id=player_data["pandascore_id"],
            team=player_data["team"],
            birth_city=player_data["birth_city"],
            college=player_data["college"],
            gsis_id=player_data["gsis_id"],
            rotoworld_id=player_data["rotoworld_id"],
            number=player_data["number"],
            age=player_data["age"],
        )


def contains_letter(s: str) -> bool:
    """Check if string contains letters.

    Args:
        s (str): Value

    Returns:
        bool: True if alpha, False if numerical
    """
    return any(char.isalpha() for char in s)


class PlayerNotFoundError(KeyError):
    """Player not found in database."
    """
    def __init__(self, player_id):
        super().__init__(f"Player with ID {player_id} not found.")
        

class Player:
    """Constructs player model based on player ID.
    """
    def __init__(self, player_id: str) -> None:
        self._id = player_id
        #self.player_db = Path("script/resources/players_db.json")
        parser = SleeperAPIParser()
        db = parser.fetch_all_players()
        try:
            found_player = db[self.id]
        except KeyError as e:
            raise PlayerNotFoundError(self._id) from e
        self.name = ""
        #TODO: Create PlayerModel for DEF
        if not contains_letter(self.id):
            self._player = PlayerFullModel.from_dict(found_player)
            self.name = self.player.personal.names.full_name
            #print("Found player: ", self.player.personal.names.full_name)
        else:
            def_player = PlayerFullModel.from_dict(found_player)
            print("Test")
 
    @property
    def id(self) -> str:
        """Sleeper ID of the Player."""
        return self._id

    @property
    def player(self) -> PlayerFullModel:
        """Personal data of the Player."""
        return self._player
    
    def __str__(self) -> str:
        return f"{self.name} {self.player.professional.position.name} {self.player.professional.team}"
    
    def __repr__(self):
        return f"{self.name} ({self.player.professional.position.name})"