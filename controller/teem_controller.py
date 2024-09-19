from dataclasses import asdict

from flask import Blueprint, jsonify, request
from toolz import pipe
from toolz.curried import reduce

from repository.player_repository import get_player_by_id
from repository.teem_repository import get_all_teems, create_teem, update_teem
from model.teem_model import Teem

# from repository.teem_repository import get_all_answers
# from repository.season_repository import get_all_questions, create_question
# from service.player_service import create_full_question_on_db

teems_blueprint = Blueprint("teems",__name__)

@teems_blueprint.route("/", methods=['GET'])
def get_all():
    teems = list(map(asdict, get_all_teems()))
    return jsonify(teems), 200


@teems_blueprint.route("/", methods=['POST'])
def create():
    try:
        all_data = request.json
        # Create the question using the data from the request
        li = all_data["player_ids"]
        data = reduce(lambda res, next: {*res, get_player_by_id(next).positions } ,li,{})
        if len(data) < 5:
            return jsonify({"error": f"{list(data)}"})
        new_teem = Teem(all_data["team_name"],li[0],li[1],li[2],li[3],li[4])
        teem = create_teem(new_teem)
        return jsonify(asdict(teem)), 201
    except Exception as e:
        return jsonify({"error": str(e)}),400


@teems_blueprint.route("/", methods=['PUT'])
def put():
    try:
        teem_id = request.args.get("teem_id")
        all_data = request.json
        # Create the question using the data from the request
        li = all_data["player_ids"]
        data = reduce(lambda res, next: {*res, get_player_by_id(next).positions}, li, {})
        if len(data) < 5:
            return jsonify({"error": f"{list(data)}"})
        new_teem = Teem("__", li[0], li[1], li[2], li[3], li[4])
        new_teem.id = int(teem_id)
        teem = update_teem(new_teem)
        return jsonify(asdict(teem)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


