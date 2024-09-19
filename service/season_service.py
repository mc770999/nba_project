from toolz import pipe,reduce, partial
from toolz.curried import partial

from model.season_model import Season

# Season:
#    id: None
#    player_id: None
#    position: str
#    age: int
#    games: int
#    games_started: int
#    minutes_pg: float
#    field_goals: int
#    field_attempts: int
#    field_percent: float
#    three_fg: int
#    three_attempts: int
#    three_percent: float
#    two_fg: int
#    two_attempts: int
#    two_percent: float
#    effective_fg_percent: float
#    ft: int
#    ft_attempts: int
#    ft_percent: float
#    offensive_rb: int
#    defensive_rb: int
#    total_rb: int
#    assists: int
#    steals: int
#    blocks: int
#    turnovers: int
#    personal_fouls: int
#    points: int
#    team: str
#    season: int
#

# "id": 18229,
#     "playerName": "A.J. Green",
#     "position": "SG",
#     "age": 24,
#     "games": 56,
#     "gamesStarted": 0,
#     "minutesPg": 614.0,
#     "fieldGoals": 83,
#     "fieldAttempts": 196,
#     "fieldPercent": 0.423,
#     "threeFg": 69,
#     "threeAttempts": 169,
#     "threePercent": 0.408,
#     "twoFg": 14,
#     "twoAttempts": 27,
#     "twoPercent": 0.519,
#     "effectFgPercent": 0.599,
#     "ft": 17,
#     "ftAttempts": 19,
#     "ftPercent": 0.895,
#     "offensiveRb": 9,
#     "defensiveRb": 55,
#     "totalRb": 64,
#     "assists": 30,
#     "steals": 9,
#     "blocks": 4,
#     "turnovers": 12,
#     "personalFouls": 49,
#     "points": 252,
#     "team": "MIL",
#     "season": 2024,
#     "playerId": "greenaj01"

def convert_to_season(json,p_id):
    return Season(player_id=p_id,position=json["position"],
                  games_started=json["gamesStarted"],games=json["games"],
                    age=json["age"],two_fg=json["twoFg"],
                    three_percent=json["threePercent"],three_attempts=json["threeAttempts"],
                    three_fg=json["threeFg"],field_percent=json["fieldPercent"],
                    field_attempts=json["fieldAttempts"],field_goals=json["fieldGoals"],
                    minutes_pg=json["minutesPg"],total_rb=json["totalRb"],
                    defensive_rb=json["defensiveRb"],offensive_rb=json["offensiveRb"],
                  ft_percent=json["ftPercent"],ft_attempts=json["ftAttempts"],
                    ft=json["ft"],effective_fg_percent=json["effectFgPercent"],
                    two_percent=json["twoPercent"],two_attempts=json["twoAttempts"],
                    season=json["season"],team=json["team"],
                  points=json["points"],personal_fouls=json["personalFouls"],
                  turnovers=json["turnovers"],blocks=json["blocks"],
                    steals=json["steals"],assists=json["assists"]
                  )




#[{true},{false},{false}]
#[(0,{true}),(1,{false}),{false}]
