from dataclasses import asdict

from flask import Blueprint, jsonify, request
from toolz import pipe
from toolz.curried import reduce

from repository.player_repository import get_player_by_id
from repository.teem_repository import get_all_teems, create_teem
from model.teem_model import Teem

# from repository.teem_repository import get_all_answers
# from repository.season_repository import get_all_questions, create_question
# from service.player_service import create_full_question_on_db

teems_blueprint = Blueprint("teems",__name__)

@teems_blueprint.route("/", methods=['GET'])
def get_all():
    breakpoint()
    teems = list(map(asdict, get_all_teems()))
    return jsonify(teems), 200


@teems_blueprint.route("/", methods=['POST'])
def create():
    try:
        all_data = request.json
        breakpoint()
        # Create the question using the data from the request
        li = all_data["player_ids"]
        data = reduce(lambda res, next: {*res, get_player_by_id(next).positions } ,li,{})
        if len(data) < 5:
            return jsonify({"error": "not valid players"})
        data = list(data)
        new_teem = Teem(all_data["team_name"],li[0],li[1],li[2],li[3],li[4])
        t_id = create_teem(new_teem)
        new_teem.id = t_id
        return jsonify(asdict(new_teem)), 201
    except Exception as e:
        return jsonify({"error": str(e)}),
