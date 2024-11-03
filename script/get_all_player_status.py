from script.api_parser import SleeperAPIParser
from script.leagues.leagues import League
from typing import List, Dict, Any

class Parser:
    #TODO :Rename this class
    def __init__(self, user_id: str) -> None:
        self.parser = SleeperAPIParser()
        self.user_id = user_id

    @property
    def leagues(self) -> List[League]:
        """List of all user leagues.
        """
        leagues = self.parser.get_all_leagues_for_user(self.user_id)
        return [League.from_dict(x) for x in leagues]
    

def main():

    parser = Parser()
    #Tested, returns list of League objects
    user_leagues = parser.leagues
