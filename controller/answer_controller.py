from dataclasses import asdict

from flask import Blueprint, jsonify, request


from repository.season_repository import get_season_and_player

season_blueprint = Blueprint("answers", __name__)

@season_blueprint.route("/", methods=['GET'])
def get_all(year,position):
    fighters = list(map(asdict, get_season_and_player))
    return jsonify(fighters), 200




