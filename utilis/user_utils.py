from operator import itemgetter

from toolz.curried import partial,pipe


def get_atr(season):
    return {**season, "atr" : season["assists"] / (season["turnovers"] + 0.00000000000000000001)  }

def get_average(season):
    all_average = pipe(
        season,
        lambda li: map(lambda dict1:  dict1["points"] / dict1["games"] ,li),
        list,
        lambda li : sum(li) / len(li)
    )
    return all_average

def add_ppg(player,season):
    return {**player, "ppg_ratio" : (player["points"] / player["games"]) / get_average(season)}