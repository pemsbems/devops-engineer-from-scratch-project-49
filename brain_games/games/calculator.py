import random

from brain_games.main_engine import game_engine


def task():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    question = f"{num1} {operator} {num2}"
    correct_answer = str(result)

    return [question, correct_answer]


def run_game():
    rules = "What is the result of the expression?"
    game_engine(task, rules)