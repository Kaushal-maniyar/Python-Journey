import html


class Question:
    def __init__(self, text, answer):
        self.text = html.unescape(text)
        self.answer = answer


class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.current_ans = ""

    def still_has_question(self):
        total_question = len(self.question_list)
        return self.question_no < total_question

    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        self.current_ans = question.answer
        return f"Q.{self.question_no} : {question.text}? "

    def check_answer(self):
        return self.current_ans
