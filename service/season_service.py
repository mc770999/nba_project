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

def convert_to_season(json,p_id):
    return Season(player_id=p_id,position=json["position"],
                  games_started=json["games_started"],games=json["games"],
                    age=json["age"],two_fg=json["two_fg"],
                    three_percent=json["three_percent"],three_attempts=json["three_attempts"],
                    three_fg=json["three_fg"],field_percent=json["field_percent"],
                    field_attempts=json["field_attempts"],field_goals=json["field_goals"],
                    minutes_pg=json["minutes_pg"],total_rb=json["total_rb"],
                    defensive_rb=json["defensive_rb"],offensive_rb=json["offensive_rb"],
                  ft_percent=json["ft_percent"],ft_attempts=json["ft_attempts"],
                    ft=json["ft"],effective_fg_percent=json["effective_fg_percent"],
                    two_percent=json["two_percent"],two_attempts=json["two_attempts"],
                    season=json["season"],team=json["team"],
                  points=json["points"],personal_fouls=json["personal_fouls"],
                  turnovers=json["turnovers"],blocks=json["blocks"],
                    steals=json["steals"],assists=json["assists"]
                  )




#[{true},{false},{false}]
#[(0,{true}),(1,{false}),{false}]
