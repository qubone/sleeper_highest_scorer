from enum import Enum

class SleeperAPI:
    """Constants related to the Sleeper API.

    Returns:
        _type_: _description_
    """
    TEST = ""


class InjuryNotes(Enum):
    """Different injury notes.
    """
    SURGERY = "Surgery"
    SPRAIN = "Sprain"
    FRACTURE = "Fracture"
    STRAIN = "Strain"
    SORENESS = "Soreness"
    STINGER = "Stringer"
    RUPTURED = "Ruptured"
    INFLAMMATION = "Inflammation"
    BRUISE = "Bruise"


class InjuryStatus(Enum):
    """Injury status.
    """
    QUESTIONABLE = "Questionable"
    DOUBTFUL = "Doubtful"
    IR = "IR"
    OUT = "Out"
    NA = "NA"


class InjuryBodyPart(Enum):
    """Injured body parts of a player.
    """
    ACHILLES = "Achilles"
    ANKLE = "Ankle"
    BACK = "Back"
    BICEPS = "Biceps"
    CALF = "Calf"
    CHEST = "Chest"
    COACHS_DECISION = "Coach's Decision"
    CONCUSSION = "Concussion"
    ELBOW = "Elbow"
    FINGER = "Finger"
    FOOT = "Foot"
    FOREARM = "Forearm"
    GROIN = "Groin"
    HAMSTRING = "Hamstring"
    HAND = "Hand"
    HEAD = "Head"
    HEEL = "Heel"
    HIP = "Hip"
    ILLNESS = "Illness"
    KNEE = "Knee"
    KNEE_ACL = "Knee - ACL"
    KNEE_ACL_MCL = "Knee - ACL + MCL"
    KNEE_MCL = "Knee - MCL"
    KNEE_MENISCUS = "Knee - Meniscus"
    LEG = "Leg"
    LOWER_BODY = "Lower Body"
    LOWER_LEG = "Lower Leg"
    NECK = "Neck"
    PECTORAL = "Pectoral"
    PERSONAL = "Personal"
    QUADRICEPS = "Quadriceps"
    RIBS = "Ribs"
    SHOULDER = "Shoulder"
    SHOULDER_AC_JOINT = "Shoulder - AC Joint"
    SHOULDER_LABRUM = "Shoulder - Labrum"
    SUSPENSION = "Suspension"
    THUMB = "Thumb"
    TOE = "Toe"
    UNDISCLOSED = "Undisclosed"
    UPPER_BODY = "Upper Body"
    WRIST = "Wrist"


class Status(Enum):
    """Activity status.
    """
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class NFLPosition(Enum):
    """Player position.
    """
    QB = "QB"
    WR = "WR"
    RB = "RB"
    TE = "TE"
    K = "K"
    DEF = "DEF"

def map_position(position_name: str):
    try:
        # Attempt to match the position name with an Enum member
        return NFLPosition[position_name.replace(" ", "_").upper()].value
    except KeyError:
        return "Unknown Position"
