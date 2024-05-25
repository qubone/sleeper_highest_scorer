"""Handling of Sleeper user data."""
from typing import Dict, Any
from script.avatars.avatar import SleeperAvatar


class SleeperUser:
    '''
    Via the user resource, you can GET the user object
    by either providing the username or user_id of the user. '''
    def __init__(self, user_data: Dict[str, Any]) -> None:
        self._user_name = user_data.get("username")
        self._user_id = user_data.get("user_id")
        self._is_bot = user_data.get("is_bot")
        self._display_name = user_data.get("display_name")
        self._avatar = SleeperAvatar(user_data.get("avatar"))

    @property
    def user_name(self) -> str:
        """Returns the Sleeper user name."""
        return self._user_name

    @property
    def user_id(self) -> str:
        """Returns the Sleeper user ID."""
        return self._user_id

    @property
    def is_bot(self) -> bool:
        """Returns if User is bot."""
        return self._is_bot

    @property
    def display_name(self) -> str:
        """Returns Sleeper display name."""
        return self._display_name

    @property
    def avatar(self) -> SleeperAvatar:
        """Returns Sleeper avatar."""
        return self._avatar
