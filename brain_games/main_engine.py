import prompt

from brain_games.cli import welcome_user


def game_engine(get_task, rules):
    name = welcome_user()
    print(f"Hello, {name}!")
    print(rules)

    goal = 0
    winning = 3
    while goal < winning:
        result = get_task()
        question = result[0]
        true = result[1]
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == true:
            print("Correct!")
            goal = goal + 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{true}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")