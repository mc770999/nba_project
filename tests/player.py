import pytest
from repository.database import create_all_tables, drop_all_tables
from repository.player_repository import *

from model.player_model import Player
from repository.sead import seed

@pytest.fixture(scope="module")
def setup_database():
    create_all_tables()
    seed()
    # drop_all_tables()

def test_create_team_player(setup_database):
    new_id = create_player(Player(name="Sp",positions="sg"))
    assert new_id >=1

def test_get_all_team_player(setup_database):
    players = get_all_players()
    assert players

def test_get_player_by_id(setup_database):
    player = get_player_by_id(1)
    assert player.id == 1

def test_get_player_by_name(setup_database):
    player = get_player_by_name("sp")
    assert player

