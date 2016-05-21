# encoding: utf-8
from lol_api.api._champion import Champion
from lol_api.api._championmastery import ChampionMastery
from lol_api.api._current_game import CurrentGame
from lol_api.api._featured_games import FeaturedGames
from lol_api.api._game import Game
from lol_api.api._league import League
from lol_api.api._lol_status import LolStatus
from lol_api.api._match import Match
from lol_api.api._matchlist import Matchlist
from lol_api.api._stats import Stats
from lol_api.api._summoner import Summoner
from lol_api.api._team import Team

from lol_api.api._lol_static_data import LolStaticData
from lol_api._client import Client
from lol_api._local_data import LocalData
from lol_api._utils import RateLimitWatcher


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
    assert isinstance(c.FeaturedGames, FeaturedGames)
