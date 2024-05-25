"""Handling of all data related to leagues."""
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Type, TypeVar

from script.leagues.rosters import LeagueRoster
from script.parser.api_parser import SleeperAPIParser
from script.players.player_types import (Bench, Flex, Kicker, Quarterback,
                                         RunnningBack, SuperFlex, TightEnd,
                                         WideReceiver)
from script.players.players import Player

TRUE = 1
FALSE = 0


T = TypeVar('T', bound=Enum)


class RosterPosition(Enum):
    """Handling of roster position data from Sleeper API."""
    QB = 'QB'
    RB = 'RB'
    WR = 'WR'
    TE = 'TE'
    FLEX = 'FLEX'
    SUPER_FLEX = 'SUPER_FLEX'
    DEF = 'DEF'
    K = 'K'
    BN = 'BN'

    @classmethod
    def validate(cls: Type[T], value: str) -> bool:
        return value in (v for v in cls._value2member_map_)


class LeagueType(Enum):
    """Handling of league type from Sleeper API."""
    REDRAFT = 0
    KEEPER = 1
    DYNASTY = 2

    @classmethod
    def validate(cls, value):
        return value in cls.__members__

    """ 
    def validate_color(value):
    try:
        color = Color[value]
        return True
    except KeyError:
        return False
    
        
    def validate_color(value):
    return value in Color.__members__
    """


class ReceivingScoring():
    """Handling of receiving score data."""
    def __init__(self, score_settings: Dict[str, float]) -> None:
        self.rec: float = score_settings.get('playoff_week_start')
        self.rec_yd: float = score_settings.get('playoff_week_start')
        self.rec_td: float = score_settings.get('playoff_week_start')
        self.bonus_rec_te: float = score_settings.get('playoff_week_start')
        self.rec_2pt: float = score_settings.get('playoff_week_start')


@dataclass
class PassingScoring():
    """Handling of passing score data."""
    def __init__(self, score_settings) -> None:
        self.pass_yd = score_settings.get('playoff_week_start')
        self.pass_td = score_settings.get('playoff_week_start')
        self.pass_2pt = score_settings.get('playoff_week_start')


@dataclass
class RushingScoring():
    """Handling of rushing score data."""
    def __init__(self, score_settings) -> None:
        self.rush_yd: float = score_settings.get('playoff_week_start')
        self.rush_td: float = score_settings.get('playoff_week_start')
        self.rush_2pt: float = score_settings.get('playoff_week_start')


@dataclass
class Defense():
    """Handling of defense score data."""
    def __init__(self, score_settings: Dict[str, float]) -> None:
        self.def_td: float = score_settings.get('def_td')
        self.safe: float = score_settings.get('safe')
        self.pts_allow_0: float = score_settings.get('pts_allow_0')
        self.pts_allow_1_6: float = score_settings.get('pts_allow_1_6')
        self.pts_allow_7_13: float = score_settings.get('pts_allow_7_13')
        self.pts_allow_14_20: float = score_settings.get('pts_allow_14_20')
        self.pts_allow_21_17: float = score_settings.get('pts_allow_21_17')
        self.pts_allow_28_34: float = score_settings.get('pts_allow_28_34')
        self.pts_allow_35p: float = score_settings.get('pts_allow_35p')
        # TODO: Clean up


@dataclass
class SpecialTeams():
    """Handling of special teams data."""
    def __init__(self, score_settings: Dict[str, float]) -> None:
        self.st_td: float = score_settings.get('st_td')
        self.st_ff: float = score_settings.get('st_ff')
        self.st_fum_rec: float = score_settings.get('st_fum_rec')
        self.def_st_fum_rec: float = score_settings.get('def_st_fum_rec')
        self.def_st_ff: float = score_settings.get('def_st_ff')
        self.def_st_td: float = score_settings.get('def_st_td')
        self.blk_kick: float = score_settings.get('blk_kick')


@dataclass
class Kicking:
    """Handling of placekicker data."""
    def __init__(self, score_settings: Dict[str, float]) -> None:
        self.fgmiss: float = score_settings.get('fgmiss')
        self.fgm_0_19: float = score_settings.get('fgm_0_19')
        self.fgm_20_29: float = score_settings.get('fgm_20_29')
        self.fgm_30_39: float = score_settings.get('fgm_30_39')
        self.fgm_40_49: float = score_settings.get('fgm_40_49')
        self.fgm_50p: float = score_settings.get('fgm_50p')
        self.xpm: float = score_settings.get('xpm')
        self.xpmiss: float = score_settings.get('xpmiss')
        # TODO: Clean up


@dataclass
class CustomSettings:
    """Handling of custom scoring data."""
    def __init__(self, score_settings: Dict[str, Any]) -> None:
        self.rush_td_40p: float = score_settings.get('rush_td_40p')
        self.rush_td_50p: float = score_settings.get('rush_td_50p')
        self.rec_td_40p: float = score_settings.get('rec_td_40p')
        self.rec_td_50p: float = score_settings.get('rec_td_50p')


class LeagueType(Enum):
    REDRAFT = 0
    KEEPER  = 1
    DYNASTY = 2

class ScoringSettings():
    """Entry point for league scoring settings."""
    def __init__(self, score_settings: Dict[str, float]) -> None:
        self._rec_settings = ReceivingScoring(score_settings)
        self._rush_settings = RushingScoring(score_settings)
        self._pass_settings = PassingScoring(score_settings)
        self._def_settings = Defense(score_settings)
        self._st_settings = SpecialTeams(score_settings)
        self._kicking_settings = Kicking(score_settings)
        self._custom_settings = CustomSettings(score_settings)

    @property
    def receiving_settings(self):
        """Returns receiving score settings."""
        return self._rec_settings

    @property
    def rushing_settings(self):
        """Returns rushing score settings."""
        return self._rush_settings

    @property
    def passing_settings(self):
        """Returns passing score settings."""
        return self._pass_settings

    @property
    def defense_settings(self):
        """Returns defense score settings."""
        return self._def_settings

    @property
    def special_teams_settings(self):
        """Returns special teams score settings."""
        return self._st_settings

    @property
    def kicking_settings(self):
        """Returns special teams score settings."""
        return self._kicking_settings

    @property
    def custom_settings(self):
        """Returns custom score settings."""
        return self._custom_settings


class WaiverType(Enum):
    """Handling of league type from Sleeper API."""
    ROLLING_WAIVERS = 0
    REVERSE_STANDINGS = 1
    FAAB_BIDDING = 2


class LeagueWaiverType():
    """Gets the league waiver type."""
    def __init__(self, settings: Dict[str, Any]) -> None:
        self.settings = settings
        self._waiver_type = None

    def is_rolling_waivers(self) -> bool:
        """Checks if the waiver type is rolling waivers."""
        self.waiver_type = self.settings.get(
            'waiver_type'
            ) == WaiverType.ROLLING_WAIVERS
        return self.waiver_type

    def is_reverse_standings(self) -> bool:
        """Checks if the waiver type is reverse standings."""
        self.waiver_type = self.settings.get(
            'waiver_type'
            ) == WaiverType.REVERSE_STANDINGS
        return self.waiver_type

    def is_faab_bidding(self) -> bool:
        """Checks if the waiver type is FAAB bidding."""
        self.waiver_type = self.settings.get(
            'waiver_type'
            ) == WaiverType.FAAB_BIDDING
        return self.waiver_type

    @property
    def waiver_type(self) -> WaiverType:
        """Returns the enum type."""
        return self._waiver_type


@dataclass
class LeagueDraftData():
    """Handling of league draft settings."""
    def __init__(self, settings: Dict[str, int]) -> None:
        self.draft_rounds: int #= settings.get('draft_rounds')
        self.taxi_years: int #= settings.get('taxi_years')
        self.pick_trading: int #= settings.get('pick_trading')


class PlayoffSeedType(Enum):
    """Handling of league type from Sleeper API."""
    DEFAULT = 0
    RE_SEED = 1


class LeaguePlayoffData():
    """Handling of league playoff settings."""
    def __init__(self, settings: Dict[str, int]) -> None:
        self.playoff_teams: int = settings.get('playoff_teams')
        self.playoff_type: int = settings.get('playoff_type')
        self.playoff_week_start: int = settings.get('playoff_week_start')
        self.playoff_round_type: int = settings.get('playoff_round_type')
        self.playoff_seed_type: int = settings.get('playoff_seed_type')

    def is_default_seeding(self) -> bool:
        """Returns true if default seeding."""
        return self.playoff_seed_type == PlayoffSeedType.DEFAULT

    def is_re_seeding(self) -> bool:
        """Returns true if default seeding."""
        return self.playoff_seed_type == PlayoffSeedType.RE_SEED


@dataclass
class LeagueWaiverData():
    """Handling of league waiver settings."""
    def __init__(self, settings: Dict[str, int]) -> None:
        self.waiver_type = LeagueWaiverType(settings.get('waiver_type'))
        self.daily_waivers_last_ran = settings.get('daily_waivers_last_ran')
        self.waiver_day_of_week = settings.get('waiver_day_of_week')
        self.waiver_clear_days = settings.get('waiver_clear_days')
        self.waiver_budget = settings.get('waiver_budget')
        self.waiver_bid_min: int = settings.get('waiver_bid_min')
        self.daily_waivers_days: int = settings.get('daily_waivers_days')
        self.daily_waivers: int = settings.get('daily_waivers')
        # TODO: Clean up


@dataclass
class LeagueRosterSettings():
    """Handling of league roster settings."""
    def __init__(self, settings: Dict[str, int]) -> None:
        self.bench_lock: int = settings.get('bench_lock')
        self.offseason_adds: int = settings.get('offseason_adds')
        self.taxi_deadline: int = settings.get('taxi_deadline')
        self.taxi_slots: int = settings.get('taxi_slots')
        self.taxi_allow_vets: int = settings.get('taxi_allow_vets')


@dataclass
class LeagueTradeSettings():
    """Handling of league trade settings."""
    def __init__(self, settings: Dict[str, int]) -> None:
        self.trade_review_days: int = settings.get('trade_review_days')
        self.trade_deadline: int = settings.get('trade_deadline')
        self.disable_trades: int = settings.get('disable_trades')


class LeagueTopSettings():
    """Handling of high level league settings."""
    def __init__(self, settings: Dict[str, int]) -> None:
        self.start_week: int = settings.get('start_week')
        self.type: LeagueType = settings.get('type')
        self._num_teams: int = settings.get('num_teams')
        self.best_ball: int = settings.get('best_ball')

    def is_best_ball(self) -> bool:
        """Returns true if league is best ball."""
        return self.best_ball == TRUE

    def is_redraft(self) -> bool:
        """Returns true if league is redraft."""
        return self.type == LeagueType.REDRAFT

    def is_keeper(self) -> bool:
        """Returns true if league is keeper."""
        return self.type == LeagueType.KEEPER

    def is_dynasty(self) -> bool:
        """Returns true if league is dynasty."""
        return self.type == LeagueType.DYNASTY

    @property
    def number_of_teams(self) -> int:
        """Returns league size."""
        return self._num_teams


@dataclass
class LeagueSettingsNew():
    """Entry point for league settings."""
    def __init__(self, settings: Dict[str, int]) -> None:
        self._top_settings = LeagueTopSettings(settings)
        self._waiver_settings = LeagueWaiverData(settings)
        self._draft_settings = LeagueDraftData(settings)
        self._playoff_settings = LeaguePlayoffData(settings)
        self._roster_settings = LeagueRosterSettings(settings)
        self._trade_settings = LeagueTradeSettings(settings)

    @property
    def top_settings(self) -> LeagueTopSettings:
        """Returns league top settings."""
        return self._top_settings

    @property
    def waiver_settings(self) -> LeagueWaiverData:
        """Returns league waiver settings."""
        return self._waiver_settings

    @property
    def draft_settings(self) -> LeagueDraftData:
        """Returns league draft settings."""
        return self._draft_settings

    @property
    def playoff_settings(self) -> LeaguePlayoffData:
        """Returns league playoff settings."""
        return self._playoff_settings

    @property
    def roster_settings(self) -> LeagueRosterSettings:
        """Returns league roster settings."""
        return self._roster_settings

    @property
    def trade_settings(self) -> LeagueTradeSettings:
        """Returns league trade settings."""
        return self._trade_settings


class LeagueMetadata():
    """Handling of league meta data."""
    def __init__(self, meta_data: dict) -> None:
        self.latest_league_winner_roster_id: str = meta_data.get(
            'latest_league_winner_roster_id'
            )
        self.keeper_deadline: str = meta_data.get('keeper_deadline')
        self.copy_from_league_id: str = meta_data.get('copy_from_league_id')
        self.auto_continue: str = meta_data.get('auto_continue')


class LeagueTopData():
    """Handling league top data."""
    def __init__(self, league_data: Dict[str, Any]) -> None:
        self.name: str = league_data.get('name')
        self.status: str = league_data.get('status')
        self.season: str = league_data.get('season')
        self.season_type: str = league_data.get('season_type')
        self.sport: str = league_data.get('sport')
        self.avatar: str = league_data.get('avatar')
        self.total_rosters: int = league_data.get('total_rosters')

    def get_name(self):
        """Returns the league name."""
        return self.name

    def get_status(self):
        """Returns the league status."""
        return self.status

    def get_season(self):
        """Returns the number of rosters in a league."""
        return self.season

    def get_season_type(self):
        """Returns the league season type."""
        return self.season_type

    def get_sport(self):
        """Returns the league sport."""
        return self.sport

    def get_avatar(self):
        """Returns the league avatar."""
        return self.avatar

    def get_total_rosters(self):
        """Returns the number of rosters in a league."""
        return self.total_rosters


@dataclass
class LeagueBracketData():
    """Handling league bracket data."""
    def __init__(self, league_data: Dict[str, Any]) -> None:
        self.loser_bracket_id: str = league_data.get('loser_bracket_id')
        self.bracket_id: str = league_data.get('bracket_id')
        self.group_id: str = league_data.get('group_id')


class LeaguePositions:
    """Handling of league position data."""
    def __init__(self, roster_positions: List[str]) -> List[str]:
        self.roster_position_data = roster_positions
        self._roster_positions = []

    def add_player(self) -> List[Player]:
        """Parses the players of a roster and
        appends the player types to a list."""
        for pos in self.roster_position_data:
            if pos == RosterPosition.QB:
                self._roster_positions.append(Quarterback)
            elif pos == RosterPosition.RB:
                self._roster_positions.append(RunnningBack)
            elif pos == RosterPosition.WR:
                self._roster_positions.append(WideReceiver)
            elif pos == RosterPosition.TE:
                self._roster_positions.append(TightEnd)
            elif pos == RosterPosition.FLEX:
                self._roster_positions.append(Flex)
            elif pos == RosterPosition.SUPER_FLEX:
                self._roster_positions.append(SuperFlex)
            elif pos == RosterPosition.DEF:
                self._roster_positions.append(Defense)
            elif pos == RosterPosition.K:
                self._roster_positions.append(Kicker)
            elif pos == RosterPosition.BN:
                self._roster_positions.append(Bench)
            else:
                raise ValueError("No valid player type found.")

    @property
    def roster_positions(self):
        """Returns the positions of a roster."""
        return self._roster_positions


class League:
    """Main class for a League.

    League data is retrieved in JSON format using HTTP get
    Using league_id as input.

    """
    def __init__(self, league_data: Dict[str, Any]) -> None:
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
        self._metadata = LeagueMetadata(league_data.get('metadata'))

    @property
    def league_id(self) -> str:
        """Returns the league ID."""
        return self._league_id

    @property
    def draft_id(self) -> str:
        """Returns the draft ID."""
        return self._draft_id

    @property
    def roster_positions(self) -> LeaguePositions:
        """Returns the roster positions."""
        return self._roster_positions

    @property
    def bracket_data(self) -> LeagueBracketData:
        """Returns the league bracket data. ."""
        return self._bracket_data

    @property
    def scoring_settings(self) -> ScoringSettings:
        """Returns the league score settings."""
        return self._scoring_settings

    @property
    def league_settings(self) -> LeagueSettingsNew:
        """Returns the league settings."""
        return self._league_settings

    @property
    def metadata(self) -> LeagueMetadata:
        """Returns the league metadata."""
        return self._metadata


class LeagueParse:
    """This endpoint retrieves a specific league."""
    def __init__(self, league_id: str) -> None:
        self.league_id = league_id
        self.parser = SleeperAPIParser()

    def get_league(self) -> League:
        """Returns the League data for given league."""
        data = self.parser.get_league(self.league_id)
        return League(data)

    def get_rosters(self) -> List[LeagueRoster]:
        """Returns all rosters from a league."""
        rosters = []
        league_rosters = self.parser.get_league_rosters(self.league_id)
        for roster in league_rosters:
            rosters.append(LeagueRoster(roster))
        return rosters
