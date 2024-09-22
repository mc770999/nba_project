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
        FOREIGN KEY (player_1) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (player_2) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (player_3) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (player_4) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (player_5) REFERENCES players(id) ON DELETE CASCADE
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
    ) returning id;
    """, (teem.name, teem.player_1,teem.player_2,teem.player_3,teem.player_4,teem.player_5))
    new_id = cursor.fetchone()["id"]
    teem.id = new_id
    connection.commit()
    cursor.close()
    connection.close()
    return teem

def get_all_teems() -> List[Teem]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        select * from teems
        """)
    res = cursor.fetchall()
    teems = [Teem(**u) for  u in res]
    cursor.close()
    connection.close()
    return teems


def update_teem(teem: Teem) -> None:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE teems
    SET 
        player_1 = %s,
        player_2 = %s,
        player_3 = %s,
        player_4 = %s,
        player_5 = %s
    WHERE id = %s returning id;
    """, (teem.player_1, teem.player_2, teem.player_3, teem.player_4, teem.player_5, teem.id))
    connection.commit()
    cursor.close()
    connection.close()
    return teem

def get_teem_by_id(u_id : int) -> Teem:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
            select * from teems where id = (%s)
            """,(u_id,))
    res = cursor.fetchone()
    teem = Teem(**res)
    cursor.close()
    connection.close()
    return teem


#
def delete_teem(u_id : int) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    DELETE FROM teems
    WHERE id = (%s);
    """, (u_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return u_id
