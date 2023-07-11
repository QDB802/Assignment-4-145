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
            input_file: The initial maze file that will be converted
        Return:
            A list of lists which contain the maze layout
    """
    f = open(input_maze, "r")
    lines = f.readlines()
    # This list comprehension is used to strip away all
    maze = [[value for value in line.rstrip() if value != ' '] for line in lines]
    f.close()
    return maze


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

    # If the maze's start and end are at the exact same position, it will convert the location to a 'P' then
    # output the finished maze.
    if current_row == target_row and current_col == target_col:
        g = open(output_file_name, 'w')
        maze_list[current_row][current_col] = 'P'
        for row in maze_list:
            g.write(' '.join(row) + '\n')







SolveMaze("Maze1.txt", (1,1), (1,1))