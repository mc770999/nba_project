from repository.player_repository import create_players_tables
from repository.season_repository import create_seasons_tables, get_db_connection
from repository.teem_repository import create_teem_tables


def create_all_tables():
    create_players_tables()
    create_teem_tables()
    create_seasons_tables()

def drop_all_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Dropping tables in the correct order due to foreign key dependencies
    cursor.execute('''
        DROP TABLE IF EXISTS seasons;
        DROP TABLE IF EXISTS teems;
        DROP TABLE IF EXISTS players;
    ''')

    connection.commit()
    cursor.close()
    connection.close()
