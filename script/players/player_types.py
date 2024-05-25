from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any


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


@dataclass
class OffensivePlayer():
    ''' Base class for offense player scoring settings. '''
    def __init__(self, score_settings) -> None:
        self.fum: float = score_settings['fum']
        self.fum_lost: float = score_settings['fum_lost']


@dataclass
class DefensivePlayer():
    ''' Base class for defensive player. '''
    def __init__(self, score_settings) -> None:
        self.int = score_settings['int']
        self.fumble_recs = score_settings['']
        self.sacks = score_settings['sack']
        self.tackle = score_settings['tackle']
        self.ff = score_settings['ff']
        self.fum_rec = score_settings['fum_rec']
        self.fum_rec_td = score_settings['fum_rec_td']


class Quarterback(OffensivePlayer):
    def __init__(self) -> None:
        pass


class RunnningBack(OffensivePlayer):
    def __init__(self) -> None:
        pass


class WideReceiver(OffensivePlayer):
    def __init__(self) -> None:
        pass


class TightEnd(OffensivePlayer):
    def __init__(self) -> None:
        pass


class Kicker():
    def __init__(self) -> None:
        pass

class Flex():
    def __init__() -> None:
        pass

class SuperFlex():
    def __init__(self) -> None:
        pass

class Bench():
    def __init__(self) -> None:
        pass

class LeagueType(Enum):
    ''' Handling of league type from Sleeper API. '''
    REDRAFT = 0
    KEEPER = 1
    DYNASTY = 2


class Receiving(OffensivePlayer):
    ''' Handling of receiving data. '''
    def __init__(self, score_settings: Dict[str, Any]) -> None:
        super(OffensivePlayer, self).__init__()
        self.rec: float = score_settings.get('playoff_week_start')
        self.rec_yd: float = score_settings.get('playoff_week_start')
        self.rec_td: float = score_settings.get('playoff_week_start')
        self.bonus_rec_te: float = score_settings.get('playoff_week_start')
        self.rec_2pt: float = score_settings.get('playoff_week_start')


class Passing(OffensivePlayer):
    ''' Handling of passing data. '''
    def __init__(self, score_settings: Dict[str, Any]) -> None:
        super(OffensivePlayer, self).__init__()
        self.pass_yd = score_settings.get('pass_yd')
        self.pass_td = score_settings.get('pass_td')
        self.pass_2pt = score_settings.get('pass_2pt')
    
    def get_pass_yards(self):
        ''' Returns number of passing yards. '''
        return self.pass_yd
    
    def get_pass_td(self):
        ''' Returns number of passing touchdowns. '''
        return self.pass_td
    
    def get_pass_2pt(self):
        ''' Returns number of two-point conversions. '''
        return self.pass_2pt


class Rushing(OffensivePlayer):
    ''' Handling of rushing data. '''
    def __init__(self, score_settings) -> None:
        super(OffensivePlayer, self).__init__()
        self.rush_yd: float = score_settings.get('playoff_week_start')
        self.rush_td: float = score_settings.get('playoff_week_start')
        self.rush_2pt: float = score_settings.get('playoff_week_start')

    def get_rushing_yards(self):
        ''' Returns the total rushing yards by a player. '''
        return self.rush_yd

    def get_rushing_touchdowns(self):
        ''' Returns the total rushing touchdowns by a player. '''
        return self.rush_td

    def get_rushing_2pt_conversions(self):
        ''' Returns the total rushing 2 point conversions by a player. '''
        return self.rush_yd
    

doc_results = dict()
results = 12

doc_results = {"doc": results}