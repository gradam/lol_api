# encoding: utf-8
from riotApi._api_client import Client
from riotApi._utils import RateLimitWatcher
from riotApi._champion import Champion
from riotApi._championmastery import ChampionMastery
from riotApi._current_game import CurrentGame
from riotApi._game import Game
from riotApi._league import League
from riotApi._local_data import LocalData
from riotApi._lol_static_data import LolStaticData
from riotApi._lol_status import LolStatus
from riotApi._match import Match
from riotApi._matchlist import Matchlist
from riotApi._stats import Stats
from riotApi._summoner import Summoner
from riotApi._team import Team


def test_object_create():
    c = Client('test_api_key', 'eune')
    assert c.api_key == 'test_api_key'
    assert isinstance(c.watcher, RateLimitWatcher)
    assert isinstance(c.LolStaticData, LolStaticData)
    assert isinstance(c.LocalData, LocalData)
    assert isinstance(c.Champion, Champion)
    assert isinstance(c.Championmastery, ChampionMastery)
    assert isinstance(c.CurrentGame, CurrentGame)
    assert isinstance(c.Game, Game)
    assert isinstance(c.League, League)
    assert isinstance(c.LolStatus, LolStatus)
    assert isinstance(c.Match, Match)
    assert isinstance(c.Matchlist, Matchlist)
    assert isinstance(c.Stats, Stats)
    assert isinstance(c.Summoner, Summoner)
    assert isinstance(c.Team, Team)
