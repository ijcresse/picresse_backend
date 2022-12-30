#puzzle management functions

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