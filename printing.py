# Printing functions
import reports


def count_games_print(file_name):
    games_count = reports.count_games(file_name)
    print(f'How many games are in the file?     {games_count}')

def decide_print(file_name):
    game_year = input("What year you are looking for? ")
    is_year_in_file = reports.decide(file_name, game_year)
    if is_year_in_file == True:
        print(f"Game from Year {game_year} is in file")
    else:
        print(f"Game from Year {game_year} isn't in file")

def get_latest_print(file_name):
    latest_game_title = reports.get_latest(file_name)
    print(f"Title of the latest game is: {latest_game_title}")

