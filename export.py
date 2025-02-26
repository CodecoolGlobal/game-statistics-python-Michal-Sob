
# Export functions

import sys
import reports

def export(exported_file):
    file_name = sys.argv[1]
    year = sys.argv[2]
    genre = sys.argv[3]
    title = sys.argv[4]
    with open(exported_file, 'w') as file:
        file.write(
f"""{file_name}
{str(reports.count_games(file_name))}
{str(reports.decide(file_name, year))}
{str(reports.get_latest(file_name))}
{str(reports.count_by_genre(file_name, genre))}
{str(reports.get_line_number_by_title(file_name, title))}
{str(reports.sort_abc(file_name))[1:-1]}    #[1:-1] is deleting squared brackets
{str(reports.get_most_played(file_name))}
{str(reports.sum_sold(file_name))}
{str(reports.get_selling_avg(file_name))}
{str(reports.count_longest_title(file_name))}
{str(reports.get_date_avg(file_name))}
{str(reports.get_game(file_name, title))}
""")




export(input('Enter new file name: '))