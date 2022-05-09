import random
from data import question_data
from quiz_brain import Question


def prepare_question_bank():
    random.shuffle(question_data)
    my_list = []
    for question in question_data:
        que = Question(question['question'], question['correct_answer'])
        my_list.append(que)
    return my_list
