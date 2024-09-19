import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI
from model.player_model import Player
from typing import List


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI,cursor_factory=RealDictCursor)

def create_players_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    player_name VARCHAR(255) UNIQUE NOT NULL
);
    )
        """
    )
    conn.commit()
    cur.close()
    conn.close()


def create_player(player : Player) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    insert into players (name) 
    values (%s,) returning id
    """,(player.name,))
    new_id = cursor.fetchone()["id"]
    connection.commit()
    cursor.close()
    connection.close()
    return new_id

def get_all_players() -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        select * from players
        """)
    res = cursor.fetchall()
    users = [Player(**u) for  u in res]
    cursor.close()
    connection.close()
    return users


def get_player_by_id(u_id : int) -> Player:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
            select * from users where id = (%s)
            """,(u_id,))
    res = cursor.fetchone()
    user = Player(**res)
    cursor.close()
    connection.close()
    return user


