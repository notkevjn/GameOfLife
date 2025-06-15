import random

#def dead_state(height, width):
#    board = []
#    for i in range (height):
#
 #       row = []
#
 #       for i in range (width):
  #          row.append(0)
   #     board.append(row)
#
 #   return board



def random_state(height, width):
    board = []
    for i in range (height):

        row = [] # Create lists depending on height

        for i in range (width):
            row.append(random.randint(0, 1)) # Append random Value to each index in the list
        board.append(row) # Append finished list to the whole board

    return board


def render(board):
    for row in board:

        symbol = "|" # left wall

        for cell in row:
            if cell == 1:
                symbol += " #" # Alive Cell
            else:
                symbol += "  " # Dead Cell

        symbol += "|"  # right wall

        print(symbol)


def next_board_state(initial_board_state):
    new_board_state = []

    cell_dies = [0,1]
    cell_lives = [2,3]
    cell_overpop = [4,5,6,7,8]
    cell_revive =  [3]

    for row_idx in range(len(initial_board_state)): # iterate through the rows 
        new_row = []

        for col_idx in range(len(initial_board_state[0])): # iterate through the columns
            cell = initial_board_state[row_idx][col_idx] # get the value of the determined cell (alive/dead)

            live_neighbours = 0

            for row in [-1, 0, 1]:  # Loop over possible neighbours
                for column in [-1, 0, 1]:
                    neighbour_row = row_idx + row 
                    neighbour_col = col_idx + column
                    
                    if row == 0 and column == 0:  # exclude Cell itself
                        continue

                    elif 0 <= neighbour_row < len(initial_board_state) and 0 <= neighbour_col < len(initial_board_state[0]):  # exclude out of bounds indexes
                        
                        if initial_board_state[neighbour_row][neighbour_col] == 1:  # increase live neighbours count for calculation later
                            live_neighbours += 1

            if live_neighbours in cell_dies:  # Game of Life Logic
                cell = 0
            if live_neighbours in cell_lives and cell == 1:
                cell = 1
            if live_neighbours in cell_overpop:
                cell = 0
            if live_neighbours in cell_revive and cell == 0:
                cell = 1

            new_row.append(cell)

        new_board_state.append (new_row)

    return new_board_state
                        
                        # print (f"cell: {cell} {initial_board_state[neighbour_row][neighbour_col]}")
        



if __name__ == "__main__":
    board = random_state(10,10)
    print("Random board:")
    render(board)
    print("Next Board State:")
    next_board = next_board_state(board)
    render(next_board)
    print("Next Board State:")
    for gen in range(20):
        print (f"generation: {gen+1}")
        next_board = next_board_state(next_board)
        render(next_board)
        