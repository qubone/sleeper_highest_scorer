"""Handling of Sleeper Avatar data"""


class SleeperAvatar:
    """Users and leagues have avatar images.
    There are thumbnail and full-size images for each avatar."""
    def __init__(self, avatar_id: str) -> None:
        self._avatar_id = avatar_id
        self._avatar_url = f'https://sleepercdn.com/avatars/{avatar_id}'
        self._avatar_thumb_url = f'https://sleepercdn.com/avatars/thumbs/{avatar_id}'

    @property
    def avatar_id(self) -> str:
        """Returns the avatar id."""
        return self._avatar_id

    @property
    def avatar_url(self) -> str:
        """Returns the avatar id url."""
        return self._avatar_url

    @property
    def avatar_thumb_url(self) -> str:
        """Returns the avatar thumbnail url."""
        return self._avatar_thumb_url
