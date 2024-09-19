from repository.player_repository import create_player
from service.season_service import convert_to_answers
from model.player_model import Player
from model.teem_model import Teem

from typing import List


def create_player_and_season_on_db(json) -> None:
    player = _convert_player_model(json)
    p_id = create_player(player)
    answers : List[Answer] = convert_to_season(json ,q_id)
    for answer in answers:
        create_answer(answer)
    return q_id




def _convert_player_model(json):
    return Player(json["playerName"])

