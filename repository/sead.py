from api.api import get_season
from repository.player_repository import create_players_tables
from repository.season_repository import create_seasons_tables
from repository.teem_repository import create_teem_tables
from service.player_service import create_player_and_season_on_db


def seed():
    try:
        create_players_tables()
        create_teem_tables()
        create_seasons_tables()
        list_json = get_season(2024),
        for season in list_json[0]:
            create_player_and_season_on_db(season)
        list_json = get_season(2023),
        for season in list_json[0]:
            create_player_and_season_on_db(season)
        list_json = get_season(2022),
        for season in list_json[0]:
            create_player_and_season_on_db(season)
    except Exception as e:
        print(e,"errur")







