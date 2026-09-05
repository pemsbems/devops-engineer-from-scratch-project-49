import random

from brain_games.main_engine import game_engine


def task():
    num = random.randint(1, 100)
    question = str(num)

    if num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return [question, correct_answer]


def run_game():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_engine(task, rules)