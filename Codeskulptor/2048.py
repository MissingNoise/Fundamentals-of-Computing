"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # Removes and adds zeros in new_list from list
    count = line.count(0)
    new_line = filter(lambda a: a != 0, line)
    for number in range(count):
        new_line.append(0)
    # iterates through new_line and merges pairs
    for number in range(len(line)-1):
        if new_line[number] is 0:
            continue
        if new_line[number] == new_line[number + 1]:
            new_line.pop(number + 1)
            new_line[number] = new_line[number] * 2
            new_line.append(0)
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.cells = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for row in self.cells:
            print str(row)
        return "Printed values in the grid"

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction==LEFT or direction==UP:
            row = 0
            col = 0
        if direction==RIGHT:
            row = 0
            col = self.grid_width - 1
        if direction==DOWN:
            row = self.grid_height - 1
            col = 0
        changed = 0
        while 0<=row<self.grid_height and 0<=col<self.grid_width:
            currentrow = row
            currentcol = col
            line = []
            while 0<=currentrow<self.grid_height and 0<=currentcol<self.grid_width:
                line += [self.get_tile(currentrow,currentcol)]
                currentrow += OFFSETS[direction][0]
                currentcol += OFFSETS[direction][1]
            currentrow = row
            currentcol = col
            newline = merge(line)
            if newline!=line:
                changed += 1
            idx = 0
            while 0<=currentrow<self.grid_height and 0<=currentcol<self.grid_width:
                self.set_tile(currentrow,currentcol,newline[idx])
                currentrow += OFFSETS[direction][0]
                currentcol += OFFSETS[direction][1]
                idx += 1
            row += 1 - abs(OFFSETS[direction][0])
            col += 1 - abs(OFFSETS[direction][1])
        if changed>0:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        if random.random()<0.9:
            value = 2
        else:
            value = 4
            
        zero_values = []
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.cells[row][col] == 0:
                    zero_values.append([row, col])
                    
        if not zero_values:
            print "There is no space left"
        else:
            tile = random.choice(zero_values)
            
            self.set_tile(tile[0], tile[1], value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.cells[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


