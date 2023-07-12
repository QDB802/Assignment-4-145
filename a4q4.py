# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# CMPT 145
# Instructor: Lauresa Stilling


def maze_conversion(input_maze):
    """
        Purpose:
            Converts the initial maze file into a list of lists maze.
        Parameters:
            input_maze: The initial maze file that will be converted
        Return:
            A list of lists which contain the maze layout
    """
    f = open(input_maze, "r")
    lines = f.readlines()
    # This list comprehension is used to strip away all whitspace and then paste it properly into list of lists.
    maze = [[value for value in line.rstrip() if value != ' '] for line in lines]
    f.close()
    return maze


def move_validity(lst, current_row, current_col):
    """
        Purpose:
            Checks the validity of the current move in order to determine if the move is allowed.
        Parameters:
            lst: The maze list of lists.
            current_row: An integer of the current row position.
            current_col: An integer of the current column position.
        Return:
            A Boolean determining the move validity, True for a valid move, False for an invalid move.
    """
    row_numbers = len(lst)
    col_numbers = len(lst[1])
    if current_row < 0 or current_row >= row_numbers:
        return False
    elif current_col < 0 or current_col >= col_numbers:
        return False
    if lst[current_row][current_col] != '0':
        return False
    else:
        return True


def SolveMaze(maze_list, current, goal):
    """
    Purpose:
        Iterates through the maze list and determines the way to get out of it.
    Parameters:
        maze_list: The initial maze file to be converted into the list of lists and explored.
        current: A tuple of the starting position or current position for the maze.
        goal: A tuple of the ending coordinates.
    Return:
    """
    # Converts the tuples into single coordinates.
    for i in maze_list:
        print(*i)
    print("\n")
    target_row, target_col = goal

    # If the maze's current position and end are at the exact same position, it will convert the location to a 'P', then
    # output the finished maze.
    if current[0] == target_row and current[1] == target_col:
        return True

    # Checks the move validity to ensure move is not going out of bounds or repeating.
    if not move_validity(maze_list, current[0], current[1]):
        return False

    maze_list[current[0]][current[1]] = "P"

    for ra, ca in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        new_row = current[0] + ra
        new_col = current[1] + ca
        if new_row < 6 and new_col < 6:
            if SolveMaze(maze_list, (new_row, new_col), goal):
                return True

    maze_list[current[0]][current[1]] = '0'
    return False


maze = maze_conversion("Maze1.txt")
if SolveMaze(maze, (0, 3), (4, 5)):
    for row in maze:
        print(" ".join(str(cell) for cell in row))
else:
    print("No path exists.")

