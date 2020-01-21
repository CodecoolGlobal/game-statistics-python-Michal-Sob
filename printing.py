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
    print(f"{title} line number is: {line_number}")

def sort_abc_print(file_name):
    sorted_file = reports.sort_abc(file_name)
    print(sorted_file)

def get_most_played_print(file_name):
    most_played_game = reports.get_most_played(file_name)
    print(f"The Most played Game is: {most_played_game}")

def sum_sold_print(file_name):    
    sum_sold = reports.sum_sold(file_name)
    print(f"Games total sold count is: {sum_sold}")

def get_selling_avg_print(file_name)
    avg_selling_count = reports.get_selling_avg(file_name)
    print(f"Average selling count is: {avg_selling_count}")

# 'game_stat.txt'


def main():
    dict_menu = {'1': count_games_print,
                '2': decide_print,
                '3': get_latest_print,
                '4': count_by_genre,
                '5': get_line_number_by_title_print,
                '6': sort_abc_print,
                '7': get_most_played_print,
                '8': sum_sold_print,
                '9': get_selling_avg_print}
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
                (7) Most Played Game
                (8) Total Number of sold copies
                (9) Average selling count
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
        input("\nEnter anything to go back to the menu: ")



if __name__ == "__main__":
    main()

