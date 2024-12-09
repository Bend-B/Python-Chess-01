import os
import math

def coords_to_index(x, y):
    # Ensure x and y are within bounds for an 8x8 grid
    if 0 <= x < 8 and 0 <= y < 8:
        index = (y * 8) + x
        return index
    else:
        raise ValueError(f"Invalid coordinates: ({x}, {y})")



def index_to_coords(z):
    y = math.floor(z / 8)
    x = z - (y * 8)
    return(x, y)


def piece_color(x):
    if x != 0:
        if x > 6:
            return(2) # Black
        else:
            return(1) # White
    else:
        return(0) # Blank
    

def is_even(x):
    return x % 2 == 0


def coords_to_screen(x, y):
    x = 100 + (x * 75)
    y = y * 75
    return(x, y)


def obsruct_check(game, x, y, piece_id):

    target_index = coords_to_index(x, y)
    if game[target_index] != 0:
        if piece_color(game[target_index]) == piece_color(piece_id):
            return(0, True)
        else:
            return(1, True)
    else:
        return(1, False)

        


class Piece:
    def __init__(self):
        pass


    def pawn_moves(game, piece_id, piece_index):

        moves = [0] * 64
        start_pos = 0

        x, y = index_to_coords(piece_index)

        if piece_color(piece_id) == 2: # Black
            d = (-1)
            opp = 1
            start_pos = 6
        elif piece_color(piece_id) == 1: # White
            d = 1 
            opp = 2
            start_pos = 1
        else:
            d = 0
            opp = 0
            start_pos = 0

        if y == start_pos: # If on starting pos
              # Check if both squares ahead are empty
            if 0 <= x < 8 and 0 <= y + (d * 2) < 8:
                if game[coords_to_index(x, y + (d * 2))] == 0 and game[coords_to_index(x, y + d)] == 0:
                    moves[coords_to_index(x, y + (d * 2))] = 1

             

        # Check if the square ahead is empty
        if 0 <= x < 8 and 0 <= y + d < 8:
            if game[coords_to_index(x, y + d)] == 0: 
                moves[coords_to_index(x, y + d)] = 1 

        if 0 <= x + 1 < 8 and 0 <= y + d < 8:  # Diagonal to the Right
            if piece_color(game[coords_to_index(x + 1, y + d)]) == opp:
                moves[coords_to_index(x + 1, y + d)] = 1

        if 0 <= x - 1 < 8 and 0 <= y + d < 8:  # Diagonal to the Left
            if piece_color(game[coords_to_index(x - 1, y + d)]) == opp:
                moves[coords_to_index(x - 1, y + d)] = 1
                
        return moves
    
    def rook_moves(game, piece_id, piece_index):
    
        moves = [0] * 64

        x, y = index_to_coords(piece_index)

        # Directions [right]   [left]   [up]    [down]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for dx, dy in directions:

            i, j = x, y

            while True:
                i += dx
                j += dy

                if i < 0 or i >= 8 or j < 0 or j >= 8:
                    break
                
                move, stop = obsruct_check(game, i, j, piece_id)
                moves[coords_to_index(i, j)] = move

                if stop:
                    break
                
        return(moves)

    def knight_moves(game, piece_id, piece_index):
    
        moves = [0] * 64
        x, y = index_to_coords(piece_index)

        # Directions [up, left], [up, right], [right, up], [left, down]
        # Directions [down, left] [down, right] [right, down] [left, up]
        directions = [(1, 2), (-1, 2), (-2, 1), (2, -1),
                    (1, -2), (-1, -2), (-2, -1), (2, 1)]

        for z in directions:
            (i, j) = z
            i += x
            j += y
        
            if 0 <= i < 8 and 0 <= j < 8:
                move, stop = obsruct_check(game, i, j, piece_id)
                moves[coords_to_index(i, j)] = move
    
        return moves

    def bishop_moves(game, piece_id, piece_index):
    
        moves = [0] * 64

        x, y = index_to_coords(piece_index)

        # Directions [top right], [bottom left], [top left], [bottom right]
        directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        for dx, dy in directions:

            i, j = x, y

            while True:
                i += dx
                j += dy

                if i < 0 or i >= 8 or j < 0 or j >= 8:
                    break
                
                move, stop = obsruct_check(game, i, j, piece_id)
                moves[coords_to_index(i, j)] = move

                if stop:
                    break
                
        return(moves)
    

    def queen_moves(game, piece_id, piece_index):

        moves = [0] * 64

        x, y = index_to_coords(piece_index)
    
        # Directions [top right], [bottom left], [top left], [bottom right]
        directions = [(1, 1), (-1, -1), (-1, 1), (1, -1)]

        for dx, dy in directions:

            i, j = x, y

            while True:
                i += dx
                j += dy

                if i < 0 or i >= 8 or j < 0 or j >= 8:
                    break
                
                move, stop = obsruct_check(game, i, j, piece_id)
                moves[coords_to_index(i, j)] = move

                if stop:
                    break

        # Directions [right]   [left]   [up]    [down]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:

            i, j = x, y

            while True:
                i += dx
                j += dy

                if i < 0 or i >= 8 or j < 0 or j >= 8:
                    break
                
                move, stop = obsruct_check(game, i, j, piece_id)
                moves[coords_to_index(i, j)] = move

                if stop:
                    break

        return(moves)
    

    def king_moves(game, piece_id, piece_index):
    
        moves = [0] * 64
        x, y = index_to_coords(piece_index)

        # Directions [left], [left up], [up], [right up]
        # Directions [right] [right down] [down] [left down]
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1),
                    (-1, 0), (-1, -1), (0, -1), (1, -1)]

        for z in directions:
            (i, j) = z
            i += x
            j += y
        
            if 0 <= i < 8 and 0 <= j < 8:
                move, stop = obsruct_check(game, i, j, piece_id)
                moves[coords_to_index(i, j)] = move
    
        return moves


piece_moves = Piece