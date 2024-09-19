# from api.api import get_questions
# from controller.answer_controller import answers_blueprint
from repository.player_repository import drop_all_tables, get_all_players
from repository.sead import seed
# from repository.teem_repository import get_all_answers, get_answers_by_question_id
# from repository.season_repository import get_all_questions, get_question_by_id
# from repository.user_answer_repository import get_user_answer_by_id

# from repository.player_repository import get_all_users, get_user_by_id

from flask import Flask

from repository.season_repository import get_all_seasons

app = Flask(__name__)

if __name__ == "__main__":
    # drop_all_tables()
    # seed()

    print({"a" :a})
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