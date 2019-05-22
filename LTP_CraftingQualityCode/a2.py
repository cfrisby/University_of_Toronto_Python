# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, column):
        """ (Rat, str, int, int) -> NoneType

        Creates a Rat object given a 1-character symbol for the rat,
        the row where the rat is located, and the column where the rat
        is located.

        >>> Rat('P', 1, 4)
        None
        >>> Rat('J', 3, 3)
        None
        """

        self.symbol = symbol
        self.row = row
        self.col = column
        self.num_sprouts_eaten = 0

    def set_location(self, row, column):
        """ (Rat, int, int) -> NoneType

        Sets the Rat's row and col instance variables to the
        given row and column.

        >>> Rat.set_location(2, 4)
        None
        >>> Rat.set_location(1, 1)
        None
        """

        self.row = row
        self.col = column

    def eat_sprout(self):
        """ (Rat) -> NoneType

        Add 1 to the rat's instance variable num_sprouts_eaten.

        >>> Rat.eat_sprout()
        None
        """

        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the Rat, in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> print(Rat)
        'J at (4, 3) ate 2 sprouts.'
        """

        return "{} at ({}, {}) ate {} sprouts.".format(self.symbol,
               str(self.row), str(self.col), str(self.num_sprouts_eaten))

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        Creates a Maze object and initializes the four instance
        variables.

        >>> Maze([['#', '#', '#', '#', '#', '#', '#'], 
                  ['#', '.', '.', '.', '.', '.', '#'], 
                  ['#', '.', '#', '#', '#', '.', '#'], 
                  ['#', '.', '.', '@', '#', '.', '#'], 
                  ['#', '@', '#', '.', '@', '.', '#'], 
                  ['#', '#', '#', '#', '#', '#', '#']], 
                  Rat('J', 1, 1),
                  Rat('P', 1, 4))
        None
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0

        for row in maze:
            for item in row:
                if item == SPROUT:
                    self.num_sprouts_left += 1

    def is_wall(self, row, column):
        """ (Maze, int, int) -> bool

        Return True iff there is a wall at the given row and
        column of the maze.

        >>> Maze.is_wall(1, 3)
        True
        """

        return self.maze[row][column] == WALL

    def get_character(self, row, column):
        """ (Maze, int, int) -> str

        Return the character in the maze at the given row and column
        If there is a rat at that location, then return the character
        of the rat.

        >>> Maze.get_character(1, 3)
        '#'
        """

        if self.rat_1.row == row and self.rat_1.col == column:
            return self.rat_1.symbol
        elif self.rat_2.row == row and self.rat_2.col == column:
            return self.rat_2.symbol
        else:
            return self.maze[row][column]
        
    def move(self, rat, vert, horiz):
        """ (Maze, Rat, int, int) -> bool

        Move the rat in the given direction, unless there is a wall
        in the way.

        >>> Maze.move(Rat, 0, 1)
        True
        """

        new_row = rat.row + vert
        new_col = rat.col + horiz

        character = self.get_character(new_row, new_col)

        if character == WALL:
            return False
        elif character == SPROUT:
            rat.set_location(new_row, new_col)
            rat.eat_sprout()
            self.maze[new_row][new_col] = HALL
            self.num_sprouts_left -= 1
            return True
        else:
            rat.set_location(new_row, new_col)
            return True

    def __str__(self):
        """ (Maze) -> str

        Return a string representation of the Maze, in this format:

        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.

        >>> print(Maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        maze_str = ''

        for row in self.maze:
            for item in row:
                maze_str += item
            maze_str += '\n'

        return maze_str + str(self.rat_1) + '\n' + str(self.rat_2)
