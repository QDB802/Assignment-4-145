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
    # This list comprehension is used to strip away all whitespace and then paste it properly into list of lists.
    converted_maze = [[value for value in line.rstrip() if value != ' '] for line in lines]
    f.close()
    return converted_maze


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
    # Sets the size of the maze.
    row_numbers = len(lst)
    col_numbers = len(lst[1])
    # If the move exceeds the total rows, it fails.
    if current_row < 0 or current_row >= row_numbers:
        return False
    # If the move exceeds the total columns, it fails.
    if current_col < 0 or current_col >= col_numbers:
        return False
    # If the move attempts to move onto a wall or a previous explored space, it fails.
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
    target_row, target_col = goal

    # If the maze's current position and end are at the exact same position, it will convert the location to a 'P', then
    # output the finished maze.
    if current[0] == target_row and current[1] == target_col:
        maze_list[target_row][target_col] = 'P'
        return True

    # Checks the move validity to ensure move is not going out of bounds or repeating.
    if not move_validity(maze_list, current[0], current[1]):
        return False

    maze_list[current[0]][current[1]] = "P"

    # The directions that can be moved, either Up, Down, Left or Right.
    for ra, ca in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        new_row = current[0] + ra
        new_col = current[1] + ca
        if SolveMaze(maze_list, (new_row, new_col), goal):
            return True

    maze_list[current[0]][current[1]] = '0'
    return False


def main(maze_file):
    maze = maze_conversion(maze_file)
    if SolveMaze(maze, (0, 3), (4, 5)):
        for row in maze:
            print(" ".join(str(cell) for cell in row))
    else:
        print("No path exists.")

main("Maze1.txt")

