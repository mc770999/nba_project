import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI
from model.teem_model import Teem
from typing import List


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI,cursor_factory=RealDictCursor)


def create_teem_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS teems (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        player_1 INTEGER NOT NULL,
        player_2 INTEGER NOT NULL,
        player_3 INTEGER NOT NULL,
        player_4 INTEGER NOT NULL,
        player_5 INTEGER NOT NULL,
        FOREIGN KEY (position_c) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (position_sf) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (position_pf) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (position_sg) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (position_pg) REFERENCES players(id) ON DELETE CASCADE
    )
        """
    )
    conn.commit()
    cur.close()
    conn.close()



def create_teem(teem : Teem) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO teems (
    name,
    player_1,
    player_2,
    player_3,
    player_4,
    player_5
    ) VALUES (
        %s, %s, %s, %s, %s, %s
    );
    """, (teem.name, teem.position_C,teem.position_SF,teem.position_PF,teem.position_SG,teem.position_PG))
    new_id = cursor.fetchone()["id"]
    connection.commit()
    cursor.close()
    connection.close()
    return new_id

def get_all_teems() -> List[Teem]:
    connection = get_db_connection()
    cursor = connection.cursor()
    breakpoint()
    cursor.execute("""
        select * from teems
        """)
    res = cursor.fetchall()
    teems = [Teem(**u) for  u in res]
    cursor.close()
    connection.close()
    return teems


# def get_answers_by_question_id(u_id : int) -> Answer:
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("""
#             select * from answers where question_id = (%s)
#             """,(u_id,))
#     res = cursor.fetchall()
#     answers = [Answer(**u) for  u in res]
#     cursor.close()
#     connection.close()
#     return answers
#
#
#
# def delete_answer(u_id : int) -> int:
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("""
#     DELETE FROM answers
#     WHERE id = (%s);
#     """, (u_id,))
#     connection.commit()
#     cursor.close()
#     connection.close()
#     return u_id
