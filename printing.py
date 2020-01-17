# Printing functions
import reports
import os

def count_games_print(file_name):
    games_count = reports.count_games(file_name)
    print('How many games are in the file?   \n')
    print(games_count)

def decide_print(file_name):
    year = int(input("What year you are looking for? "))
    is_year_in_file = reports.decide(file_name, year)
    print('')   #blank line
    if is_year_in_file == True:
        print(f"Game from Year {year} is in file")
    else:
        print(f"Game from Year {year} isn't in file")

def get_latest_print(file_name):
    latest_game_title = reports.get_latest(file_name)
    print(f"Title of the latest game is: {latest_game_title}")

def count_by_genre(file_name):
    genre = input("What genre are you looking for? ")
    count_of_searched_genre = reports.count_by_genre(file_name, genre)
    print('')   #blank line
    if count_of_searched_genre == 1:
        print(f"Searched genre came up {count_of_searched_genre} time.")
    if count_of_searched_genre == 0:
        print(f"Searched genre is not in a file")
    else:
        print(f"Searched genre came up {count_of_searched_genre} times.")

def get_line_number_by_title_print(file_name):
    title = input("Insert title: ")
    line_number = reports.get_line_number_by_title(file_name, title)
    print(f"{title} line number is {line_number}")

def sort_abc_print(file_name):
    sorted_file = reports.sort_abc(file_name)
    print(sorted_file)

# 'game_stat.txt'


def main():
    dict_menu = {'1': count_games_print,
                '2': decide_print,
                '3': get_latest_print,
                '4': count_by_genre,
                '5': get_line_number_by_title_print,
                '6': sort_abc_print}
    file_name = input("Please enter name of the file: ")
    while True:
        try:
            print(""""
                Choose option:
                (1) Count Games
                (2) Decide
                (3) Get Latest
                (4) Count by Genre
                (5) Get line number by title
                (6) Sort alphabetically
                (0) Quit
                """)
            option = input("Please enter a number: ")
            os.system('clear')
            if option in dict_menu.keys():
                dict_menu[option](file_name)
            elif option == '0':
                break
            else:
                raise KeyError
        except KeyError:
            print("There is no such option.")
        input("\nEnter '0' to go back to menu: ")


main()

