import random
from brain_games.main_engine import game_engine


def task():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    num1 = a
    num2 = b
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    correct_answer = str(num1)
    question = f"{a} {b}"
    return question, correct_answer


def run_game():
    rules = "Find the greatest common divisor of given numbers."
    game_engine(task, rules)
