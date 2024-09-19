from dataclasses import asdict

from flask import Blueprint, jsonify, request


from repository.season_repository import get_season_and_player

player_blueprint = Blueprint("player", __name__)

@player_blueprint.route("/", methods=['GET'])
def get_all():
    year = request.args.get("year")
    position = request.args.get("position")
    fighters = get_season_and_player(year,position)
    return jsonify(fighters), 200




