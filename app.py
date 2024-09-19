# from api.api import get_questions
# from controller.answer_controller import answers_blueprint
from controller.players_controller import player_blueprint
from controller.teem_controller import teems_blueprint
from repository.player_repository import drop_all_tables, get_all_players
from repository.sead import seed
# from repository.teem_repository import get_all_answers, get_answers_by_question_id
# from repository.season_repository import get_all_questions, get_question_by_id
# from repository.user_answer_repository import get_user_answer_by_id

# from repository.player_repository import get_all_users, get_user_by_id
from repository.season_repository import get_season_and_player

from flask import Flask

from repository.season_repository import get_all_seasons, get_season_by_year_and_player_id
from repository.teem_repository import create_teem_tables

app = Flask(__name__)

if __name__ == "__main__":
    drop_all_tables()
    create_teem_tables()
    # seed()
    app.register_blueprint(player_blueprint, url_prefix="/api/players")
    app.register_blueprint(teems_blueprint, url_prefix="/api/teems")

    app.run(debug=True)
    # user = get_user_by_id(5)
    # questions = get_question_by_id(4)
    # answer = get_answers_by_question_id(5)
    # print("/" * 1000)
    # print(user)
    # print("/" * 1000)
    # print(questions)
    # print("/" * 1000)
    # print(answer)
    # app.register_blueprint(answers_blueprint, url_prefix="/api/answers")
    #
    #
    # app.run(debug=True)