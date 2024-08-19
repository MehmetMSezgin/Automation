from data import question_data
from Question_Model import Question
from QuizBrain import QuizBrain

# import Question class

"""
create question_bank , it should contain a list of question objects
each being initialized with a question and an answer
"""

question_bank = []

total_question_amount = len(question_data)
# print(total_question_amount)

for i in range(0, total_question_amount):
    q = question_data[i].get("question")
    # print(q)
    a = question_data[i].get("correct_answer")
    Question_object = Question(q, a)
    question_bank.append(Question_object)

'''
Alternative solution
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
'''

'''When we get some data from internet just convert into object and keep it like that'''

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    if not quiz.still_has_questions():
        quiz.final_score()

