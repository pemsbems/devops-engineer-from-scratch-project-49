import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def task():
    num = random.randint(1, 100)
    question = str(num)

    if num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return [question, correct_answer]


