# Report functions
file_name = 'game_stat.txt'

with open(file_name, 'r') as reader:
    result = []
    for line in reader.readlines():
        result.append(list(line.split("\t")))

def count_games(file_name):
    return sum(1 for line in open(file_name))
    

def decide(file_name, year):
    with open(file_name, 'r') as f:
        if str(year) in f.read():
            return True
        else:
            return False

def get_latest(file_name):
    current_year = int(result[0][2])
    latest_year = current_year
    for line in result:
        current_year = int(result[line][2])
        if current_year > latest_year:
            latest_year = current_year
    return latest_year





print(get_latest('game_stat.txt'))
