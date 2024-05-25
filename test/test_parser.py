from pathlib import Path
from pytest import MonkeyPatch, fixture
from script.parser.api_parser import SleeperAPIParser
import requests

from unittest.mock import MagicMock, Mock


class Setup:
    ''' Setup class for shared test input data. '''
    def __init__(self) -> None:
        self.user_name = 'Linusbo'
        self.user_id = '727977584134025216'
        self.league_id = '1004113252818726912'
        self.season = '2023'
        self.avatar = '88700289dc890fc9064fb95f84b1c3eb'
        self.test_url = 'https://api.sleeper.app/v1/user/727977584134025216/leagues/nfl/2023'
        self.database = "script/resources/players_db.json"

        self.test_user_data = {
                    "username": "linusbo",
                    "user_id": "727977584134025216",
                    "is_bot": False,
                    "display_name": "Linusbo",
                    "avatar": "88700289dc890fc9064fb95f84b1c3eb"}
        self.mocker = MagicMock()
        
        #TODO: MonkeyPatch

@fixture(name="setup")
def setup_fixture():
    ''' Pytest decorator to use shared Setup class for testing. '''
    return Setup()


def test_get_players(setup: Setup, monkeypatch: MonkeyPatch):
    #get_user_call = SleeperAPIParser().get_user(setup.user_id)
    #http_get = SleeperAPIParser()._http_get_response_data_json(setup.test_url)

    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.text = '{ \
                    "username":"linusbo", \
                    "user_id":"727977584134025216", \
                    "is_bot":false, \
                    "display_name":"Linusbo", \
                    "avatar":"88700289dc890fc9064fb95f84b1c3eb"}'
                self.ok = True
                self.status = 200
        response = MockResponse()
    monkeypatch.setattr(SleeperAPIParser()._http_get_response_data_json(setup.test_url), "get", mock_get)
    
    result, ok, status = SleeperAPIParser().get_user(setup.user_id)
    assert result == '{ \
                     "username":"linusbo", \
                     "user_id":"727977584134025216", \
                     "is_bot":false, \
                     "display_name":"Linusbo", \
                     "avatar":"88700289dc890fc9064fb95f84b1c3eb"}'
    assert ok is True
    assert status == 200


def test_get_players_using_mock(setup: Setup):
    fake_resp = Mock()
    fake_resp.json = setup.mocker(return_value=setup.test_user_data)
    fake.re




'''
def test(setup: Setup, monkeypatch: MonkeyPatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
        def __init__(self):
            self.text = '{"username":"linusbo","user_id":"727977584134025216","is_bot":false,"display_name":"Linusbo","avatar":"88700289dc890fc9064fb95f84b1c3eb"}'
            self.ok = True
            self.status = 200
        response = MockResponse()
        return response
    
    monkeypatch.setattr(requests, "get", mock_get)
    result, ok, status_code = get_players()
    assert result == "<a href.......'
    assert ok is True
    assert status_code = 200

    
    
    
    
from unittest.mock import MagickMock

mock_download = MagicMock(return_value='path/to/file.zip')
mock_unpack = MagicMock()

monkeypatch.setattr('SleeperAPIParser().get_players(), 'mock_download')

)
    
    
    
    '''