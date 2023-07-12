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
    col_numbers = len(lst[0])

    # If the move is attempting to backtrack or enter a wall, it will fail.
    if lst[current_row][current_col] != '0':
        return False
    if (current_row < 0 or current_row >= row_numbers) or (current_col < 0 or current_col >= col_numbers):
        return False
    else:
        return True


def solvemaze(maze_list, current, goal):
    """
       Purpose:
           Converts the initial maze file into a list of lists maze.
       Parameters:
           maze_list: The initial maze file to be converted into the list of lists and explored.
           current: A tuple of the starting position or current position for the maze.
           goal: A tuple of the ending coordinates.
       Return:
    """
    current_row, current_col = current
    target_row, target_col = goal

    # If the maze's current position and end are at the exact same position, it will convert the location to a 'P', then
    # output the finished maze.
    if current_row == target_row and current_col == target_col:
        maze_list[current_row][current_col] = 'P'
        return True

    # Checks the move validity to ensure move is not going out of bounds or repeating.
    if not move_validity(maze_list, current_row, current_col):
        return False
    # Sets the current space to a P, to ensure no backtracking and show where path is.
    maze_list[current_row][current_col] = "P"

    # List of Tuples containing all possible moves in the 4 directions.
    for ra, ca in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        new_row = current_row + ra
        new_col = current_col + ca
        solvemaze(maze_list, (new_row, new_col), goal)

def main():
    maze_file = "Maze1.txt"
    maze = maze_conversion(maze_file)
    start_position = (0, 3)
    goal_position = (4, 5)

    if solvemaze(maze, start_position, goal_position):
        # Using the os tools to modify the output file name for completed maze.
        file_name, file_ext = os.path.splitext(maze_file)
        output_file_name = file_name + "-completed" + file_ext

        f = open(output_file_name, 'w')
        for row in maze:
            f.write(' '.join(row) + '\n')


main()
