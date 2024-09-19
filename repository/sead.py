from service.player_service import create_full_question_on_db
from repository.season_repository import create_question, create_question_tables
from typing import List
from model.player_model import Answer
from service.season_service import convert_to_answers
from repository.teem_repository import create_answer, create_answer_tables
from service.user_service import convert_to_user
from repository.player_repository import create_user, create_players_tables
from api.api import get_users,get_questions


def seed():
    # create_question_tables()
    # create_users_tables()
    # create_answer_tables()
    
    try:
        list_json = get_questions(4)[0],
        for question in list_json:
            create_full_question_on_db(question)
    except Exception as e:
        print(e,"errur")

    try:
        list_user = get_users(20),
        for user in list_user[0]:
            create_user(convert_to_user(user))
    except Exception as e:
        print(e)







