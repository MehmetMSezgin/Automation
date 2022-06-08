from QuestionProgram import Question

qText = open("Questions.txt", "r")
List = qText.readlines()

Q1 = Question(List[0], "a")
Q2 = Question(List[1], "c")
Q3 = Question(List[2], "b")

bunchOfQuestions = [Q1, Q2, Q3]


def run_program():
    score = 0
    for QS in bunchOfQuestions:
        print(QS.prompt)
        participant_answer = str(input()).lower()
        if QS.answer == participant_answer:
            score = score + 1
    result = "Your score is " + str(score) + "/" + str(len(bunchOfQuestions))
    return result


print(run_program())
qText.close()