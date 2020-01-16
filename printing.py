# Printing functions
import reports


def count_games_print(file_name):
    games_count = reports.count_games(file_name)
    print(f'How many games are in the file?     {games_count}')

def decide_print(file_name):
    year = int(input("What year you are looking for? "))
    is_year_in_file = reports.decide(file_name, year)
    if is_year_in_file == True:
        print(f"Game from Year {year} is in file")
    else:
        print(f"Game from Year {year} isn't in file")

def get_latest_print(file_name):
    latest_game_title = reports.get_latest(file_name)
    print(f"Title of the latest game is: {latest_game_title}")

def count_by_genre(file_name):
    searched_genre = input("What genre are you looking for? ")
    count_of_searched_genre = reports.count_by_genre(file_name, searched_genre)
    if count_of_searched_genre == 1:
        print(f"Searched genre came up {count_of_searched_genre} time")
    if count_of_searched_genre == 0:
        print(f"Searched genre is not in a file")
    else:
        print(f"Searched genre came up {count_of_searched_genre} times")

def get_line_number_by_title_print(file_name):
    title = input("Insert title: ")
    line_number = reports.get_line_number_by_title(file_name, title)
    print(f"{title} line number is {line_number}")

get_line_number_by_title_print('game_stat.txt')
