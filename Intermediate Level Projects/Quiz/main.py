from make_question_bank import prepare_question_bank
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = prepare_question_bank()
quizz = QuizBrain(question_bank)
quiz_window = QuizInterface(quizz)
#while quizz.still_has_question():
#   quizz.next_question()
#print("Great, You completed the Quiz!")
#print(f"Your score : {quizz.score} / {len(question_bank)}")
