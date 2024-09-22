import pytest

from model.season_model import Season
from repository.database import create_all_tables, drop_all_tables
from repository.player_repository import *


from model.player_model import Player
from repository.sead import seed
from repository.season_repository import create_season, get_all_seasons, get_season_by_year_and_player_id, \
    get_season_and_player


@pytest.fixture(scope="module")
def setup_database():
    create_all_tables()
    seed()
    # drop_all_tables()

def test_create_team_player(setup_database):
    new_id = create_season(Season(player_id=1,position="sg",
                  games_started=5,games=4,
                    age=23,two_fg=24,
                    three_percent=54,three_attempts=85,
                    three_fg=54,field_percent=56,
                    field_attempts=4,field_goals=3,
                    minutes_pg=4,total_rb=6,
                    defensive_rb=5,offensive_rb=8,
                  ft_percent=8,ft_attempts=9,
                    ft=8,effective_fg_percent=4,
                    two_percent=3,two_attempts=8,
                    season=4,team="SEE",
                  points=4,personal_fouls=10,
                  turnovers=8,blocks=8,
                    steals=9,assists=8))
    assert new_id >=1

def test_get_all_seasons(setup_database):
    seasons = get_all_seasons()
    assert seasons

def test_get_season_by_year_and_player_id(setup_database):
    player = get_season_by_year_and_player_id(2024,2)
    assert player

def test_get_season_and_player(setup_database):
    player = get_season_and_player(2024,"SG")
    assert player



