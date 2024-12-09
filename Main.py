import pygame
import math
import os

# Import textures

from texture_file import texture_list

# Set up the constants

piece_selected = -1
mouse_down = False
fps = 60
pygame.init()   
clock = pygame.time.Clock()

player_turn = 1

game = [2, 3, 4, 6, 5, 4, 3, 2,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        7, 7, 7, 7, 7, 7, 7, 7,
        8, 9, 10, 12, 11, 10, 9, 8]

mouse = [0, 0, 0]

colors = [[255, 255, 255], [0, 0, 0]]

# Define functions for data processing

def turn_change(turn):
    if turn == 2:
        turn = 1
    else:
        turn = 2
    return(turn)


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
    if x % 2 == 0:
        return(True)
    else:
        return(False)


def coords_to_screen(x, y):
    x = x * 75
    y = y * 75
    return(x, y)


def screen_to_coords(x, y):
    x = math.floor(mouse[0] / 75)
    y = math.floor(mouse[1] / 75)
    return (x, y)


from piece_movement import piece_moves

def player_move(x, y, selected_piece):
    global player_turn
    
    piece_move_functions = {
        1: piece_moves.pawn_moves,
        7: piece_moves.pawn_moves,
        2: piece_moves.rook_moves,
        8: piece_moves.rook_moves,
        3: piece_moves.knight_moves,
        9: piece_moves.knight_moves,
        4: piece_moves.bishop_moves,
        10: piece_moves.bishop_moves,
        5: piece_moves.queen_moves,
        11: piece_moves.queen_moves,
        6: piece_moves.king_moves,
        12: piece_moves.king_moves,
        }

    piece_type = game[selected_piece]

    if piece_type in piece_move_functions:
        moves = piece_move_functions[piece_type](game, game[selected_piece], selected_piece)

        if moves[coords_to_index(x, y)] == 1:
            game[coords_to_index(x, y)] = game[selected_piece]
            game[selected_piece] = 0
            player_turn = turn_change(player_turn)



# Open and set up display

background_color = (100, 100, 100)
screen = pygame.display.set_mode(size=(800,600))
pygame.display.set_caption('Bens Chess')
screen.fill(background_color)

pygame.display.flip()

# Start the program

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    (mouse[0], mouse[1]) = pygame.mouse.get_pos()
    mouse[2] = pygame.mouse.get_pressed()

    # Ingame events are processed

    if event.type == pygame.MOUSEBUTTONDOWN:
        if mouse[0] < 600 and mouse[0] > 0 and mouse_down == False:

            select_x, select_y = screen_to_coords(mouse[0], mouse[1]) 

            if piece_selected != coords_to_index(select_x, select_y):
                if  player_turn == piece_color(game[coords_to_index(select_x, select_y)]):
                    piece_selected = coords_to_index(select_x, select_y)
                else:
                    if piece_selected != -1:
                        player_move(select_x, select_y, piece_selected)
                    piece_selected = -1
            else:
                piece_selected = -1
            mouse_down = True



    if event.type == pygame.MOUSEBUTTONUP:
        mouse_down = False

    # Print the board before the pieces.
    
    for i in range(0, 64, 1):
        (x, y) = index_to_coords(i)
        x, y = coords_to_screen(x, y)
        if is_even(x) != is_even(y):
            texture_list[13].texture_draw(x, y)
        else:
            texture_list[12].texture_draw(x, y)

    # Print the pieces

    for i in range(0, 64, 1):
        (x, y) = index_to_coords(i)
        if game[i] != 0:
            disp_x, disp_y = coords_to_screen(x, y)
            texture_list[game[i]-1].texture_draw(disp_x, disp_y)

    if piece_selected != -1:
        x, y = index_to_coords(piece_selected)
        x, y = coords_to_screen(x, y)
        texture_list[14].texture_draw(x, y)

    pygame.display.update()
    clock.tick(fps)