import random

from brain_games.main_engine import game_engine


def task():
    num = random.randint(1, 100)
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        answer = "yes"
    else:
        answer = "no"
    return str(num), answer


def run_game():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_engine(task, rules)