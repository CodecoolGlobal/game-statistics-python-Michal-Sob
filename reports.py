# Report functions

def count_games(file_name):
    counted_games = sum(1 for line in open(file_name))
    return counted_games

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
    line_number = None
    for row in list_of_games:
        if title in row[0]:
            line_number = list_of_games.index(row) + 1 #lists starts from 0
            break
    if line_number == None:
        raise ValueError
    else:
        return line_number

def sort_abc(file_name):
    list_of_games = get_list_from_file(file_name)
    sorted = []
    for line in list_of_games:
        sorted.append(line[0])
    for _ in sorted:
        for title in range(len(sorted) -1):
            if sorted[title] > sorted[title +1]:
                sorted[title], sorted[title +1] = sorted[title +1], sorted[title]
    
    return sorted

def get_most_played(file_name):
    GAME_NAME_INDEX = 0
    GAME_SOLD_COUNT = 1
    file = get_list_from_file(file_name)
    most_played = file[0][GAME_SOLD_COUNT]
    most_played_title = file[0][GAME_NAME_INDEX]
    for row in file:
        if float(row[GAME_SOLD_COUNT]) > float(most_played):
            most_played = row[GAME_SOLD_COUNT]
            most_played_title = row[GAME_NAME_INDEX]
    
    return most_played_title

def sum_sold(file_name):
    result = 0
    list_of_games = get_list_from_file(file_name)
    for row in list_of_games:
        result += float(row[1])
    return result

def get_selling_avg(file_name):
    sold_count = sum_sold(file_name)
    games_count = count_games(file_name)
    return round(sold_count / games_count, 3)

# print(get_selling_avg('game_stat.txt'))
