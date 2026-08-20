import random

import prompt

from brain_games.cli import welcome_user


def brain_even():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    true = 0

    while true < 3:
        num = random.randint(1, 100)
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")
        if num % 2 == 0:
            correct = "yes"
        else:
            correct = "no"

        if answer == correct:
            print("Correct!")
            true = true + 1
        else:
            print(
                f"'{answer}' is wrong answer ;( "
                f" Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def main():
    brain_even()


if __name__ == "__main__":
    main()
