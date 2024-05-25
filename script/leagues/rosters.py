from typing import List, Dict, Any

from script.common.common import read_json_from_file
from script.players.players import Player
from decimal import Decimal


class RosterMetadata:
    """Handling of roster metadata."""
    def __init__(self, metadata: Dict[str, str]) -> None:
        self._streak: str = metadata.get('streak')
        self._record: str = metadata.get('record')

    @property
    def winning_streak(self) -> str:
        """Returns the winning streak."""
        return self._streak

    @property
    def game_record(self) -> str:
        """Returns the win and lose record."""
        return self._record


class RosterTotalPoints:
    """Handling of scoring data of a roster.

    Reads all fantasy points scored in total during the given season.
    Data is separated into integers and decimals.
    """
    def __init__(self, settings_data: Dict[str, Any]) -> None:
        self.fpts_decimal: int = settings_data.get('fpts_decimal')
        self.fpts_against_decimal: int = settings_data.get(
            'fpts_against_decimal'
            )
        self.fpts_against: int = settings_data.get('fpts_against')
        self.fpts: int = settings_data.get('fpts')
        self.ppts_decimal: int = settings_data.get('ppts_decimal')
        self.ppts: int = settings_data.get('ppts')

    def get_fantasy_points_scored(self) -> int:
        """Gets total fantasy points scored."""
        exact_fpts = Decimal(str(self.fpts)) + Decimal(
            '.' + str(self.fpts_decimal))
        return float(exact_fpts.real)

    def get_fantasy_points_allowed(self) -> int:
        """Gets total fantasy points allowed
        by combining the integer with decimal to create a float.
        """
        exact_pts_against = Decimal(str(self.fpts_against)) + Decimal(
            '.' + str(self.fpts_against_decimal))
        return float(exact_pts_against.real)


class RosterWaiverData:
    """Handling of waiver data of a roster."""
    def __init__(self, settings_data: Dict[str, Any]) -> None:
        self._waiver_position: int = settings_data.get('waiver_position')
        self._waiver_budget_used: int = settings_data.get('waiver_budget_used')
        self._total_moves: int = settings_data.get('total_moves')

    @property
    def waiver_position(self):
        """Returns current waiver position."""
        return self._waiver_position

    @property
    def waiver_budget_used(self):
        """Returns current waiver budget used."""
        return self._waiver_budget_used

    @property
    def total_moves(self):
        """Returns current waiver moves."""
        return self._total_moves

    def to_json(self) -> Dict[str, Any]:
        """Converts data back to JSON format."""
        return {
            'waiver_position': self._waiver_position,
            'waiver_budget': self._waiver_budget_used,
            'total_moves': self._total_moves
        }


class RosterSettings:
    """Handling of all roster statistics."""
    def __init__(self, settings_data: Dict[str, Any]) -> None:
        self._wins: int = settings_data.get('wins')
        self._losses: int = settings_data.get('losses')
        self._ties: int = settings_data.get('ties')
        self._waiver_data = RosterWaiverData(settings_data)
        self._scoring_data = RosterTotalPoints(settings_data)

    @property
    def wins(self):
        """Returns number of wins."""
        return self._wins

    @property
    def losses(self):
        """Returns number of losses."""
        return self._losses

    @property
    def ties(self):
        """Returns number of ties."""
        return self._ties

    @property
    def waiver_data(self):
        """Returns the waiver data."""
        return self._waiver_data

    @property
    def scoring_data(self):
        """Returns the scoring data."""
        return self._scoring_data


class RosterPlayers:
    """Handling of roster player data."""
    def __init__(self, players: Dict[str, Any], starters: Dict[str, Any], taxi: Dict[str, Any]) -> None:
        self._players = players
        self.starters = starters
        self.taxi = taxi

    @property
    def players(self):
        ''' Returns a list of all player ids.
            This will be used to map to their entry
            in the player database. '''
        return self._players

    def get_roster_players(self, database_file: str) -> List[Player]:
        ''' Returns all players in a single roster in the league. '''
        roster_players = []
        database = read_json_from_file(database_file)
        for player in self.players:
            if player in database:
                player_data = database[player]
                roster_players.append(Player(player_data))
        return roster_players

    def get_starter_players(self, database_file: str) -> List[Player]:
        ''' Returns all current starters of a roster. '''
        starters = []
        database = read_json_from_file(database_file)
        for player in self.starters:
            if player in database:
                player_data = database[player]
                starters.append(Player(player_data))
        return starters

    def get_taxi_players(self, database_file: str) -> List[Player]:
        ''' Returns all current starters of a roster. '''
        taxi_players = []
        database = read_json_from_file(database_file)
        for player in self.starters:
            if player in database:
                player_data = database[player]
                taxi_players.append(Player(player_data))
        return taxi_players


class LeagueRoster:
    """Handling all data for a roster in a league."""
    def __init__(self, roster_data: Dict[str, Any]) -> None:
        self._settings = RosterSettings(roster_data.get('settings'))
        self._roster_id: int = roster_data.get('roster_id')
        self.owner_id: str = roster_data.get('owner_id')
        self._metadata = RosterMetadata(roster_data.get('metadata'))
        self.league_id: str = roster_data.get('league_id')
        self.co_owners = roster_data.get('co_owners')
        self._roster_players = RosterPlayers(roster_data.get('players'), roster_data.get('starters'), roster_data.get("taxi"))

    @property
    def roster_id(self) -> int:
        """Returns the roster ID."""
        return self._roster_id

    @property
    def roster_settings(self) -> RosterSettings:
        """Returns settings of a roster."""
        return self._settings

    @property
    def roster_metadata(self) -> RosterMetadata:
        """Returns metadata of a roster."""
        return self._metadata

    @property
    def roster_players(self) -> RosterPlayers:
        """Returns players of a roster."""
        return self._roster_players
