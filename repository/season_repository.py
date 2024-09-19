import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI
from model.season_model import Season
from typing import List

from utilis.user_utils import get_atr, add_ppg


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI,cursor_factory=RealDictCursor)


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

def create_seasons_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS seasons (
        id SERIAL PRIMARY KEY,
        player_id INT,
        season INT,
        position VARCHAR(50),
        age INT,
        games INT,
        games_started INT,
        minutes_pg FLOAT,
        field_goals INT,
        field_attempts INT,
        field_percent FLOAT,
        three_fg INT,
        three_attempts INT,
        three_percent FLOAT,
        two_fg INT,
        two_attempts INT,
        two_percent FLOAT,
        effective_fg_percent FLOAT,
        ft INT,
        ft_attempts INT,
        ft_percent FLOAT,
        offensive_rb INT,
        defensive_rb INT,
        total_rb INT,
        assists INT,
        steals INT,
        blocks INT,
        turnovers INT,
        personal_fouls INT,
        points INT,
        team VARCHAR(255),
        FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
    )
""")
    conn.commit()
    cur.close()
    conn.close()


def create_season(seasons : Season) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""

    INSERT INTO seasons (
        player_id, season, position, age, games, 
        games_started, minutes_pg, field_goals, field_attempts, field_percent, 
        three_fg, three_attempts, three_percent,
         two_fg,  two_attempts, two_percent, 
         effective_fg_percent, ft,  ft_attempts, 
        ft_percent,  offensive_rb, defensive_rb, total_rb, assists, 
        steals, blocks, turnovers,  personal_fouls, points, team
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    ) returning id
    """, (seasons.player_id,seasons.season,seasons.position,seasons.age,seasons.games,
          seasons.games_started,seasons.minutes_pg,seasons.field_goals,seasons.field_attempts,seasons.field_percent,
          seasons.three_fg,seasons.three_attempts,seasons.three_percent,
          seasons.two_fg,seasons.two_attempts,seasons.two_percent,
          seasons.effective_fg_percent, seasons.ft, seasons.ft_attempts,
          seasons.ft_percent, seasons.offensive_rb,
          seasons.defensive_rb, seasons.total_rb, seasons.assists,
          seasons.steals,
          seasons.blocks, seasons.turnovers, seasons.personal_fouls,
          seasons.points,seasons.team
          ))
    new_id = cursor.fetchone()["id"]
    connection.commit()
    cursor.close()
    connection.close()
    return new_id

def get_all_seasons() -> List[Season]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        select * from seasons
        """)
    res = cursor.fetchall()
    questions = [Season(**u) for u in res]
    cursor.close()
    connection.close()
    return questions


def get_season_by_year_and_player_id(s_year : int, p_id) -> Season:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
            select * from seasons where season = (%s) and player_id = (%s)
            """,(s_year,p_id))
    res = cursor.fetchone()
    question = Season(**res)
    cursor.close()
    connection.close()
    return question


def get_season_and_player(s_year : int, position : str) -> Season:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
            SELECT seasons.*, players.*
            FROM seasons
            INNER JOIN players ON seasons.player_id = players.id
            WHERE seasons.season = (%s) AND seasons.position like (%s);
            """,(s_year,position))
    res = cursor.fetchall()
    all_res = [add_ppg(get_atr({**r}),res) for r in res]
    cursor.close()
    connection.close()
    return all_res




#
# def delete_question(u_id : int) -> int:
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("""
#     DELETE FROM questions
#     WHERE id = (%s);
#     """, (u_id,))
#     connection.commit()
#     cursor.close()
#     connection.close()
#     return u_id
