# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# CMPT 145
# Instructor: Lauresa Stilling

import os as os


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
    # This list comprehension is used to strip away all
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
    row_numbers = len(lst[1])
    col_numbers = len(lst[0])

    # If the move is attempting to backtrack or enter a wall, it will fail.
    if lst[current_row][current_col] != 0:
        return False
    if (current_row < 0 or current_row >= row_numbers) or (current_col < 0 or current_col >= col_numbers):
        return False
    else:
        return True


def SolveMaze(maze, current, goal):
    """
    Purpose:
        Converts the initial maze file into a list of lists maze.
    Parameters:
        maze: The initial maze file to be converted into the list of lists and explored.
        current: A tuple of the starting position or current position for the maze.
        goal: A tuple of the ending coordinates.
    Return:
    """
    # Converts the maze into the list of lists, and converts the tuples into single coordinates.
    maze_list = maze_conversion(maze)
    current_row, current_col = current
    target_row, target_col = goal

    # Using the os tools in order to add the completed into the file name to organize the files.
    file_name, file_ext = os.path.splitext(maze)
    output_file_name = file_name + "-completed" + file_ext

    # Checks the move validity to ensure move is not going out of bounds or repeating.
    if not move_validity(maze_list, current_row, current_col):
        return False

    # If the maze's start and end are at the exact same position, it will convert the location to a 'P' then
    # output the finished maze.
    if current_row == target_row and current_col == target_col:
        g = open(output_file_name, 'w')
        maze_list[current_row][current_col] = 'P'
        for row in maze_list:
            g.write(' '.join(row) + '\n')


SolveMaze("Maze1.txt", (1, 1), (1, 1))
