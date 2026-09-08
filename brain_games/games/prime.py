import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

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


