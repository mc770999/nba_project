from dataclasses import asdict

from model.season_model import Season
from repository.player_repository import create_player, get_player_by_name
from repository.season_repository import create_season
from service.season_service import convert_to_season
from model.player_model import Player
from model.teem_model import Teem

from typing import List


def create_player_and_season_on_db(p) -> None:

    player = _convert_player_model(p)
    p_id = get_player_by_name(player.name)
    if not p_id:
        p_id = create_player(player)
    else:
        p_id = p_id.id
    season = convert_to_season(p ,p_id)
    create_season(season)





def _convert_player_model(json):
    return Player(name=json["playerName"],positions=json["position"])

