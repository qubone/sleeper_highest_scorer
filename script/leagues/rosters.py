from typing import List, Dict, Any, Optional, Union

from script.common import read_json_from_file
from script.players.players import Player, PlayerDB
from decimal import Decimal


class Metadata:
    """Handling of roster metadata."""

    def __init__(self, streak: Optional[str], record: Optional[str]) -> None:
        self._streak = streak
        self._record = record

    @property
    def winning_streak(self) -> Optional[str]:
        """Winning streak of a roster."""
        return self._streak

    @property
    def game_record(self) -> Optional[str]:
        """Win and lose record of a roster."""
        return self._record

    @classmethod
    def from_dict(cls, metadata: Optional[Dict[str, str]]):
        """Creates User object from dictionary data.

        Args:
            user_data (Dict[str, Any]): _description_

        Returns:
            _type_: _description_
        self._league_id: str = league_data.get('league_id')
        self._draft_id: str = league_data.get('draft_id')
        self._roster_positions = LeaguePositions(
            league_data.get('roster_positions')
            )
        self._bracket_data = LeagueBracketData(league_data)
        self._scoring_settings = ScoringSettings(
            league_data.get('scoring_settings')
            )
        self._league_settings = LeagueSettingsNew(league_data.get('settings'))
        self._metadata = Metadata(league_data.get('metadata'))

        """
        if metadata is not None:
            return cls(metadata.get("streak"), metadata.get("record"))
        return cls(None, None)






class TotalPoints:
    """Handling of scoring data of a roster.

    Reads all fantasy points scored and allowed in total during the given season.
    Data is separated into integers and decimals.
    """

    def __init__(self, settings_data: Dict[str, Any]) -> None:
        self.fpts_decimal: int = settings_data.get("fpts_decimal")
        self.fpts_against_decimal: int = settings_data.get("fpts_against_decimal")
        self.fpts_against: int = settings_data.get("fpts_against")
        self.fpts: int = settings_data.get("fpts")
        self.ppts_decimal: int = settings_data.get("ppts_decimal")
        self.ppts: int = settings_data.get("ppts")

    def get_fantasy_points_scored(self) -> int:
        """Gets total fantasy points scored."""
        exact_fpts = Decimal(str(self.fpts)) + Decimal("." + str(self.fpts_decimal))
        return float(exact_fpts.real)

    def get_fantasy_points_allowed(self) -> int:
        """Gets total fantasy points allowed
        by combining the integer with decimal to create a float.
        """
        exact_pts_against = Decimal(str(self.fpts_against)) + Decimal(
            "." + str(self.fpts_against_decimal)
        )
        return float(exact_pts_against.real)


class WaiverData:
    """Handling of waiver data of a roster."""
    def __init__(self, settings_data: Dict[str, Any]) -> None:
        self._waiver_position: int = settings_data.get('waiver_position')
        self._waiver_budget_used: int = settings_data.get('waiver_budget_used')
        self._total_moves: int = settings_data.get('total_moves')

    @property
    def waiver_position(self):
        """Current waiver position."""
        return self._waiver_position

    @property
    def waiver_budget_used(self):
        """Current waiver budget used."""
        return self._waiver_budget_used

    @property
    def total_moves(self):
        """Current waiver moves."""
        return self._total_moves

class Settings:
    """Handling of all roster statistics."""
    def __init__(self, settings_data: Dict[str, Any]) -> None:
        self._wins: int = settings_data.get('wins')
        self._losses: int = settings_data.get('losses')
        self._ties: int = settings_data.get('ties')
        self._waiver_data = WaiverData(settings_data)
        self._scoring_data = TotalPoints(settings_data)

    @property
    def wins(self):
        """Number of wins for a roster."""
        return self._wins

    @property
    def losses(self):
        """Number of losses for a roster."""
        return self._losses

    @property
    def ties(self):
        """Number of ties for a roster."""
        return self._ties

    @property
    def waiver_data(self):
        """Waiver data of a roster."""
        return self._waiver_data

    @property
    def scoring_data(self):
        """Scoring data of a roster."""
        return self._scoring_data


class Players:
    """Handling of roster player data.

    All players in a roster.

    All starter players in a roster.

    All taxi players in a roster.
    """

    def __init__(
        self, players: Dict[str, str], starters: Dict[str, str], taxi: Dict[str, str]
    ) -> None:
        self._players = players
        self.starters = starters
        self.taxi = taxi
        self.player_db = read_json_from_file(PlayerDB.player_db) #TODO: Read from Github

    @classmethod
    def from_dict(cls, roster_data: Dict[str, Any]):
        """Creates User object from dictionary data.

        Args:
            user_data (Dict[str, Any]): _description_

        Returns:
            _type_: _description_
        """
        return cls(
            settings=roster_data["settings"],
            roster_id=roster_data["roster_id"],
            owner_id=roster_data["owner_id"],
            metadata=roster_data["metadata"],
            league_id=roster_data["league_id"],
            co_owners=roster_data["co_owners"],
        )




    @property
    def players(self):
        """All players in a roster."""
        return self._players

    def get_roster_players(self) -> List[Player]:
        """Maps all players in roster with the player database.

        Returns:
            List[Player]: Returns a list of players
        """
        roster_players: List[Player] = []
        for player in self.players:
            if player in self.player_db:
                player_data = self.player_db[player]
                roster_players.append(Player(player_data))
        return roster_players

    def get_starter_players(self) -> List[Player]:
        """Maps all starter players in roster with the player database.

        Returns:
            List[Player]: Returns a list of starter players
        """
        starters: List[Player] = []
        for player in self.starters:
            if player in self.player_db:
                player_data = self.player_db[player]
                starters.append(Player(player_data))
        return starters

    def get_taxi_players(self) -> List[Player]:
        """Maps all taxi players in roster with the player database.

        Returns:
            List[Player]: Returns a list of taxi players
        """
        taxi_players: List[Player] = []
        for player in self.starters:
            if player in self.player_db:
                player_data = self.player_db[player]
                taxi_players.append(Player(player_data))
        return taxi_players


class Roster:
    """Handling all data for a roster in a league.
    """
    # pylint: disable=R0902, R0913
    def __init__(
        self,
        taxi: Optional[List[str]],
        starters: List[str],
        settings: Dict[str, int],
        roster_id: int,
        reserve: Optional[str],
        players: Optional[List[str]],
        player_map: Optional[Any],
        owner_id: str,
        metadata: Optional[Dict[str, str]],
        league_id: str,
        keepers: Optional[Any],
        co_owners: Optional[str],
    ) -> None:
        self._taxi = [Player(player) for player in taxi]  \
            if taxi else None
        self._starters = [Player(starter) for starter in starters]
        self._settings = Settings(settings)
        self._roster_id = roster_id
        self._reserve = reserve
        if players:
            self._players = [Player(player) for player in players]
        self._player_map = player_map
        self._owner_id = owner_id
        self._metadata = Metadata.from_dict(metadata)
        self._league_id = league_id
        self._keepers = keepers
        self._co_owners = co_owners

    @classmethod
    def from_dict(cls, roster_data: Dict[str, Any]):
        """Creates User object from dictionary data.

        Args:
            user_data (Dict[str, Any]): _description_

        Returns:
            _type_: _description_
        """
        return cls(
            taxi=roster_data["taxi"],
            starters=roster_data["starters"],
            settings=roster_data["settings"],
            roster_id=roster_data["roster_id"],
            reserve=roster_data["reserve"],
            players=roster_data.get("players"),
            player_map=roster_data["player_map"],
            owner_id=roster_data["owner_id"],
            metadata=roster_data.get("metadata"),
            league_id=roster_data["league_id"],
            keepers=roster_data["keepers"],
            co_owners=roster_data["co_owners"],
        )

    @property
    def taxi(self) -> Optional[List[Player]]:
        """List of taxi squad players.
        """
        return self._taxi

    @property
    def starters(self) -> List[Player]:
        """List of current starter players.
        """
        return self._starters

    @property
    def roster_settings(self) -> Settings:
        """Roster settings."""
        return self._settings

    @property
    def roster_id(self) -> int:
        """Roster ID.
        """
        return self._roster_id

    @property
    def players(self) -> List[Player]:
        """List of players in a roster.
        """
        return self.players

    @property
    def player_map(self) -> Optional[Any]:
        """Player map of a roster.

        Not Implemented.
        """
        return self._taxi

    @property
    def owner_id(self) -> Optional[Any]:
        """Owner ID of a roster."""
        return self._owner_id

    @property
    def metadata(self) -> Metadata:
        """Metadata containing streak and records.
        """
        return self._metadata

    @property
    def league_id(self) -> str:
        """League ID.
        """
        return self._league_id

    @property
    def keepers(self) -> Optional[Any]:
        """List of keeper players.
        """
        return self._keepers

    @property
    def co_owners(self) -> Optional[Any]:
        """Co-owners of a roster. 
       
        Not Implemented.
        """
        return self._co_owners
    
    @property
    def injury_status(self) -> str:
        injury = self.players
        for p in self.players:
            print(p.player.professional.injury.status)
        return ""

