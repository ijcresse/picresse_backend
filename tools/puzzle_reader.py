import sys

#puzzle management functions

def search_params(puzzle):
    where = []
    if (puzzle.id != None):
        where.append("c_id=")
        where.append(puzzle.id)
        where.append(',')
    if (puzzle.name != None):
        where.append("c_name=")
        where.append(puzzle.name)
        where.append(',')
    if (puzzle.creator != None):
        where.append("c_creator=")
        where.append(puzzle.creator)
        where.append(',')
    if (puzzle.puzzle != None):
        where.append("c_puzzle=")
        where.append(puzzle.puzzle)
        where.append(',')
    if (puzzle.width != None):
        where.append("c_width=")
        where.append(puzzle.width)
        where.append(',')
    if (puzzle.length != None):
        where.append("c_length=")
        where.append(puzzle.length)
        where.append(',')
    if (puzzle.is_warned != None):
        where.append("c_is_warned=")
        where.append(puzzle.is_warned)
        where.append(',')
    if (puzzle.times_completed != None and puzzle.times_completed_mod != None):
        where.append("c_times_completed")
        # { = , < , > }
        where.append(puzzle.times_completed_mod)
        where.append(puzzle.times_completed)
    
    if (where[len(where) - 1] == ','):
        where = where[:-1]
    
    return ''.join(where)

def update_params(puzzle):
    values = []
    where = "c_id=" + puzzle.id
    if (puzzle['name'] != None):
        values.append("c_name=")
        values.append('"')
        values.append(puzzle['name'])
        values.append('"')
        values.append(',')
    if (puzzle['creator'] != None):
        values.append("c_creator=")
        values.append('"')
        values.append(puzzle['creator'])
        values.append('"')
        values.append(',')
    if (puzzle['puzzle'] != None):
        values.append("c_puzzle=")
        values.append('"')
        values.append(puzzle['puzzle'])
        values.append('"')
        values.append(',c_width=')
        values.append(puzzle['puzzle'][:2])
        values.append(',c_length=')
        values.append(puzzle['puzzle'][2:2])
    if (len(values) == 0):
        raise Exception("ERROR puzzle.update_params() was not passed any values!")
    return (values, where)

# puzzles must have all params.
def post_params(puzzle):
    values = []
    try: 
        values.append('"')
        values.append(puzzle['name'])
        values.append('"')
        values.append(',')
        values.append('"')
        values.append(puzzle['creator'])
        values.append('"')
        values.append(',')
        values.append('"')
        values.append(puzzle['puzzle'])
        values.append('"')
        values.append(',')
        values.append(puzzle['puzzle'][:2].lstrip('0'))
        values.append(',')
        values.append(puzzle['puzzle'][2:4].lstrip('0'))
    except:
        raise Exception("ERROR puzzle.post_params() could not process puzzle!")
    return ''.join(values)