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


def SolveMaze(maze_list, current, goal, solve_all_paths):
    """
    Purpose:
        Iterates through the maze list and determines the way to get out of it.
    Parameters:
        maze_list: The initial maze file to be converted into the list of lists and explored.
        current: A tuple of the starting position or current position for the maze.
        goal: A tuple of the ending coordinates.
        solve_all_paths: A Boolean which determines if the program will analyze all paths or just one.
    Return:
        A Boolean if solve_all_paths is True, or a List of Lists if solve_all_paths is False.
    """
    # Converts the tuples into single coordinates.
    target_row, target_col = goal

    if solve_all_paths is True:
        # Initializes a main list to store other lists in.
        paths = []

    # If the target is a 1, always returns False or a Blank List since goal is impossible to reach.
    if maze_list[target_row][target_col] == '1':
        if solve_all_paths is True:
            # Returns the blank list since it is impossible to get to the path.
            return []
            # Simply returns False since the maze is unsolvable.
        else:
            return False

    # If the maze's current position and end are at the exact same position, it will convert the location to a 'P', then
    # output the finished maze. As well, it uses lists of lists in order to save the paths better if enabled.
    if current[0] == target_row and current[1] == target_col:
        maze_list[target_row][target_col] = 'P'
        if solve_all_paths is True:
            # Adds the target coordinates to the list of lists of all paths.
            return [[current]]
        else:
            # Returns True since it is possible to find a path.
            return True

    # Checks the move validity to ensure move is not going out of bounds or repeating.
    if not move_validity(maze_list, current[0], current[1]):
        if solve_all_paths is True:
            # If move validity fails, it doesn't add anything to the list.
            return []
        else:
            # If the move validity fails, simply returns False.
            return False

    # Changes the current space to a P
    maze_list[current[0]][current[1]] = "P"

    # The directions that can be moved, either Up, Down, Left or Right.
    for ra, ca in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        new_row = current[0] + ra
        new_col = current[1] + ca
        if solve_all_paths is True:
            # Using new_paths to add all possible paths, then adds the new path to the paths list.
            new_paths = SolveMaze(maze_list, (new_row, new_col), goal, solve_all_paths)
            for path in new_paths:
                paths.append([current] + path)
        else:
            # Searches for the single path from the new position.
            if SolveMaze(maze_list, (new_row, new_col), goal, solve_all_paths):
                return True

    maze_list[current[0]][current[1]] = '0'

    # Once a path, or all paths have been found, it exits the program.
    if solve_all_paths is True:
        return paths
    else:
        return False


def main(list_o_maze, current_coordinates, target_coordinates, solve_all_paths):
    """
        Purpose:
            Runs the SolveMaze function, then prints the resulting maze(s).
        Parameters:
            list_o_maze: The initial maze file to be converted into the list of lists and explored.
            current_coordinates: A tuple of the starting position or current position for the maze.
            target_coordinates: A tuple of the ending coordinates.
            solve_all_paths: A Boolean which determines if the program will analyze all paths or just one.
        Return:
            None
    """
    # If the solve_all_paths is set to True, it searches for all paths then prints them all.
    if solve_all_paths is True:
        if SolveMaze(list_o_maze, current_coordinates, target_coordinates, solve_all_paths):
            # Since the if statement has passed, this is all the possible paths.
            paths = SolveMaze(list_o_maze, current_coordinates, target_coordinates, solve_all_paths)
            # Prints all possible paths for a maze.
            for i, path in enumerate(paths):
                print("Path", i+1)
                maze_copy = [row[:] for row in list_o_maze]
                for position in path:
                    # For each position in the maze_copy, adds a 'P' since the coordinate
                    # was explored in the simulation.
                    maze_copy[position[0]][position[1]] = 'P'
                for row in maze_copy:
                    print(" ".join(str(cell) for cell in row))
                print("\n")
    else:
        # If the solve_all_paths is set to False, it searches for the one path, and prints it and returns True.
        if SolveMaze(list_o_maze, current_coordinates, target_coordinates, solve_all_paths):
            # Since the if condition passes, this is a possible path.
            for row in list_o_maze:
                print(" ".join(str(cell) for cell in row))


maze = maze_conversion("Maze1.txt")
start = (0, 3)
target = (4, 5)
maze_option = True
main(maze, start, target, maze_option)
