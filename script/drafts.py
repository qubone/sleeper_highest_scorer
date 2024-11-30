from script.api_parser import SleeperAPIParser

from typing import Dict, List, Any

from dataclasses import dataclass

from enum import Enum

class LeagueParse:
    """This endpoint retrieves a specific league."""
    def __init__(self, league_id: str) -> None:
        self.league_id = league_id
        self.parser = SleeperAPIParser()

    def get_draft(self):
        """Returns the League data for given league."""
        all_drafts = self.parser.get_all_drafts_for_a_league(self.league_id)
        traded_picks = self.parser.get_traded_picks_in_draft("draft_id")
        all_picks = self.parser.get_all_picks_in_draft("draft_id")
        draft = self.parser.get_specific_draft("draft_id")


@dataclass
class Slots:
    """Number of slots in draft.
    WR, TE, RB, K, FLEX, DEF, BN, SF.
    """
    wide_receiver: int
    tight_end: int
    running_back: int
    kicker: int
    flex: int
    defense: int
    bench: int
    super_flex: None

    # TODO: Check how to get super_flex slots
    # super_flex=settings.get("super_flex"),
    # self.slots_super_flex: int = 0
    # super_flex: int

    @classmethod
    def from_dict(cls, settings: Dict[str, Any]):
            
        return cls(
            settings["slots_wr"],
            settings["slots_te"],
            settings["slots_rb"],
            settings["slots_k"],
            settings["slots_flex"],
            settings["slots_def"],
            settings["slots_bn"],
            settings.get("super_flex", None),
        )

class Settings:
    """Draft settings.

    Number of teams.
    Number of slots.
    Number of rounds.
    Pick timer.
    """

    def __init__(self, teams, autostart, cpu_autopick, pick_timer, slots, rounds) -> None:
        self.teams: int = teams
        self.autostart: int = autostart
        self.cpu_autopick: int = cpu_autopick
        self.pick_timer: int = pick_timer
        self.slots = slots
        self.rounds: int = rounds

    @classmethod
    def from_dict(cls, settings: Dict[str, Any]):
        """Creates User object from dictionary data.

        Args:
            user_data (Dict[str, Any]): _description_

        Returns:
            _type_: _description_
        """

        return cls(
            settings["teams"],  # Number of teams
            settings["autostart"],  # 0 Off 1 On
            settings["cpu_autopick"],  # 0 Off 1 On
            settings["pick_timer"],
            Slots.from_dict(settings),
            settings["rounds"],
        )


class ScoringType(Enum):
    """Scoring type of league.

    Standard, 0 points per reception.

    Half-PPR, 0.5 points per reception.

    Full PPR, 1 point per reception.


    """

    PPR = "ppr"
    HALF_PPR = "half-ppr"
    STANDARD = "standard"


class Metadata:
    """Draft metadata.

    Scoring type.

    Name of league.

    Description.
    """
    def __init__(self, scoring_type: ScoringType, name, description) -> None:
        self.scoring_type = scoring_type
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, meta_data: Dict[str, Any]):
        """Creates User object from dictionary data.

        Args:
            user_data (Dict[str, Any]): _description_

        Returns:
            _type_: _description_
        """

        return cls(
            meta_data["scoring_type"],
            meta_data["name"],
            meta_data["description"],
        )


class DraftType(Enum):
    """Different draft types.

    Snake. Serpentine

    Linear. Non-snaking

    Auction. Salary Cap
    """
    SNAKE = "snake"
    LINEAR = "linear"
    AUCTION = "auction"

class Status(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
    """
    PRE_DRAFT = "pre_draft"
    DRAFTING = "drafting"
    COMPLETE = "complete"


class Draft:
    """Create a draft class object based on the dictionary data fetched from the API parser."""
    def __init__(self, draft_data: Dict[str, Any]) -> None:
        self.type: str = draft_data.get("type", "snake")
        self.status: str = draft_data.get("status", "complete")
        self.start_time: str = draft_data.get(
            "start_time", "1515"
        )  # TODO: Convert to datetime
        self.sport: str = draft_data.get("sport", "nfl")
        self.settings = Settings(draft_data["settings"])
        self.season_type: str = draft_data.get("season_type", "regular")
        self.season: str = draft_data.get("season", "2017")
        self.metadata = Metadata.from_dict(draft_data["metadata"])
        self.league_id: str = draft_data.get("league_id", "1233212323132")
        self.last_picked: int = draft_data.get("last_picked", 421421412412142)
        self.last_message_time: int = draft_data.get("last_message_time", 455453453434)
        self.last_message_id: str = draft_data.get(
            "last_message_time", "1553153531135513"
        )
        self.draft_order: Dict[str, int] = draft_data.get(
            "draft_order", {"12345": 1, "23445": 2}
        )  # This is the user_id to draft slot mapping
        self.slot_to_roster_id: Dict[str, int] = draft_data.get(
            "slot_to_roster_id", {"1": 10, "2": 3, "3": 5}
        )  # This is the draft slot to roster_id mapping, leagues have rosters which have roster_ids. Draft slot 1 will go to roster 10, draft slot 2  will go to roster 2
        self.draft_id: str = draft_data.get("draft_id", "324342432234324")
        self.creators = draft_data.get("creators")
        self.created: int = draft_data.get("created", 412412424)

    def get_draft_order():
        pass

    def get_draft_slots():
        pass
