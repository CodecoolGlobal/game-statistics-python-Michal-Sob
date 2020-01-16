# Report functions

def count_games(file_name):
    return sum(1 for line in open(file_name))
    

def decide(file_name, year):
    with open(file_name, 'r') as f:
        if str(year) in f.read():
            return True
        else:
            return False

def get_list_from_file(file_name):
    with open(file_name, 'r') as file:
        list_of_games = []
        for line in file:
            list_of_games.append(line.split("\t"))
    return list_of_games

def get_latest(file_name):
    YEAR_INDEX = 2
    list_of_games = get_list_from_file(file_name)
    current_year = int(list_of_games[0][YEAR_INDEX])
    latest_year = current_year
    for Game_info in list_of_games:
        for _ in Game_info:
            current_year = int(Game_info[YEAR_INDEX])
            if current_year > latest_year:
                # Game_info[-1] = Game_info[-1].strip()
                latest_year_game = Game_info[0]
                latest_year = current_year
    return latest_year_game


def count_by_genre(file_name, genre):
    with open(file_name, 'r') as file:
        counter = 0
        for line in file:
            if genre in line:
                counter += 1
    return counter

def get_line_number_by_title(file_name, title):
    list_of_games = get_list_from_file(file_name)
    for row in list_of_games:
        if title in row[0]:
            return list_of_games.index(row) + 1 #lists starts from 0

def sort_abc(file_name):
    list_of_games = get_list_from_file(file_name)
    sorted = []
    for line in list_of_games:
        sorted.append(line[0])
    for _ in sorted:
        for title in range(len(sorted) -1):
            if sorted[title] > sorted[title +1]:
                sorted[title], sorted[title +1] = sorted[title +1], sorted[title]
    print(sorted)

#print(get_latest('game_stat.txt'))
# print(sort_abc('game_stat.txt'))
# print(get_line_number_by_title('game_stat.txt', 'The Sims 3'))
