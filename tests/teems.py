import pytest
from repository.database import create_all_tables, drop_all_tables
from repository.teem_repository import *
from repository.sead import seed

from model.teem_model import Teem

@pytest.fixture(scope="module")
def setup_database():
    drop_all_tables()
    create_all_tables()
    seed()
    # drop_all_tables()

def test_create_team(setup_database):
    new_id = create_teem(Teem(name='ps01',player_1=1,player_2=2,player_3=4,player_4=5,player_5=11))
    assert new_id >=1

def test_get_all_teams(setup_database):
    teams = get_all_teems()
    assert teams

def test_get_team_by_id(setup_database):
    team = get_teem_by_id(1)
    assert team.id == 1

def test_update_team(setup_database):
    update_teem(Teem(id=1,name="ps",player_1=1,player_2=2,player_3=4,player_4=5,player_5=11))
    team = get_teem_by_id(1)
    assert team.name == 'ps'

def test_delete_team(setup_database):
    assert delete_teem(2)