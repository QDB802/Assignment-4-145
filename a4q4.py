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
            input_file: The initial maze file that will be converted
        Return:
            A list of lists which contain the maze layout
    """
    f = open(input_maze, "r")
    lines = f.readlines()
    maze = [[value for value in line.rstrip() if value != ' '] for line in lines]
    # This list comprehension is used to strip away all
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
    maze_list = maze_conversion(maze)
    print(maze_list)

SolveMaze("Maze1.txt", 1, 1)