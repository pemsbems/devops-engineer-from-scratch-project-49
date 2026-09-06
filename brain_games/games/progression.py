import random

from brain_games.main_engine import game_engine


def generate(start, step, length):
    progression = []
    for i in range(length):
        currentElement = start + i * step
        progression.append(currentElement)
    return progression


def task():
    length = random.randint(5, 10)  
    start = random.randint(1, 20)   
    step = random.randint(1, 10)    
    
    progression = generate(start, step, length)
    unknow_numb = random.randint(0, length - 1)
    unknow = progression[unknow_numb]
    
    progression[unknow_numb] = ".."
    
    question = " ".join(map(str, progression))
    return question, str(unknow)


def run_game():
    rules = "What number is missing in the progression?"
    game_engine(task, rules)