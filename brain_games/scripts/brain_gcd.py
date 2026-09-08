from brain_games.main_engine import game_engine
from brain_games.games.gcd import task, RULES


def main():
    game_engine(task, RULES)


if __name__ == "__main__":
    main()