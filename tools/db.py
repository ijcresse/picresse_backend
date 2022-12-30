import mariadb
import json

file = open('./constants.json')
data = json.load(file)
db_params = data['db_params']
table_scripts = data['table_scripts']

T_SCRIPT_CREATE = 0
T_SCRIPT_GET_LIST = 1
T_SCRIPT_SEARCH_LIST = 2
T_SCRIPT_POST_PUZZLE = 3
T_SCRIPT_UPDATE_PUZZLE = 4
T_SCRIPT_PUZZLE_COMPLETED = 5

def get_db_connection(user, password):
    db_params['user'] = user
    db_params['password'] = password
    return mariadb.connect(**db_params)

def get_list(pagesize, offset, connection):
    cursor = connection.cursor()
    cursor.execute(table_scripts[T_SCRIPT_GET_LIST], (pagesize, offset))
    print(cursor.statement)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def search_list(params, pagesize, offset, connection):
    cursor = connection.cursor()
    cursor.execute(table_scripts[T_SCRIPT_SEARCH_LIST], (params, pagesize, offset))
    print(cursor.statement)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def post_puzzle(puzzle, connection):
    cursor = connection.cursor()
    cursor.execute(table_scripts[T_SCRIPT_POST_PUZZLE], (puzzle,))
    print(cursor.statement)
    cursor.close()
    return True

def update_params(puzzle):
    values = []
    where = "c_id=" + puzzle.id
    if (puzzle.name != None):
        values.append("c_name=")
        values.append(puzzle.name)
        values.append(',')
    if (puzzle.creator != None):
        values.append("c_creator=")
        values.append(puzzle.creator)
        values.append(',')
    if (puzzle.puzzle != None):
        values.append("c_puzzle=")
        values.append(puzzle.puzzle)
        values.append(',c_width=')
        values.append(puzzle.puzzle[:2])
        values.append(',c_length=')
        values.append(puzzle.puzzle[2:2])
        values.append(',')
    if (len(values) == 0):
        #TODO throw exception
        a = 1
    return (values, where)

def update_puzzle(puzzle, connection):
    cursor = connection.cursor()
    (values, where) = update_params(puzzle)
    cursor.execute(table_scripts[T_SCRIPT_UPDATE_PUZZLE], (values, where))
    print(cursor.statement)
    cursor.close()
    return True

def add_puzzle_completion(id, connection):
    cursor = connection.cursor()
    cursor.execute(table_scripts[T_SCRIPT_PUZZLE_COMPLETED], (id,))
    print(cursor.statement)
    cursor.close()
    return True

# puzzles must have all params.
def post_params(puzzle):
    values = []
    values.append(puzzle.name)
    values.append(',')
    values.append(puzzle.creator)
    values.append(',')
    values.append(puzzle.puzzle)
    values.append(',')
    values.append(puzzle.puzzle[:2])
    values.append(',')
    values.append(puzzle.puzzle[2:2])
    values.append(',')
    values.append('0;')
    return ''.join(values)

def post_puzzle(puzzle, connection):
    cursor = connection.cursor()
    values = post_params(puzzle)
    cursor.execute(table_scripts[T_SCRIPT_POST_PUZZLE], (values,))
    print(cursor.statement)
    cursor.close()
    return True

def close_db_connection(connection):
    connection.close()
