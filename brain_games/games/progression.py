import random

RULES = "What number is missing in the progression?"

def generate(start, step, length):
    progression = []
    for i in range(length):
        current_element = start + i * step
        progression.append(current_element)
    return progression


def task():
    length = random.randint(5, 10)  
    start = random.randint(1, 20)   
    step = random.randint(1, 10)    
    
    progression = generate(start, step, length)
    hidden_index = random.randint(0, length - 1)
    hidden_number = progression[hidden_index]
    
    progression[hidden_index] = ".."
    
    question = " ".join(map(str, progression))
    return question, str(hidden_number)


def run_game():
    rules = "What number is missing in the progression?"
    game_engine(task, rules)