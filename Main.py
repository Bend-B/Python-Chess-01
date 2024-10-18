import pygame
import math
import os

# Import textures

class Texture:
    def __init__(self, image, piece_id):
         self.image = image
         self.piece_id = piece_id
        
    def texture_draw(self, x, y):
        screen.blit(self.image, (x, y))


Texture_White_Tile = Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Tile.png')), 0)
Texture_Black_Tile = Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Tile.png')), 0)
Texture_White_King = Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-King.png')), 6)
Texture_Black_King = Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-King.png')), 12)
Texture_White_Queen = Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Queen.png')), 5)
Texture_Black_Queen = Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Queen.png')), 11)
Texture_White_Bishop = Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Bishop.png')), 4)
Texture_Black_Bishop = Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Bishop.png')), 10)
Texture_White_Knight = Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Knight.png')), 3)
Texture_Black_Knight = Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Knight.png')), 9)
Texture_White_Rook = Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Rook.png')), 2)
Texture_Black_Rook = Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Rook.png')), 8)
Texture_White_Pawn = Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Pawn.png')), 1)
Texture_Black_Pawn = Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Pawn.png')), 7)

# Set up the constants

fps = 60
pygame.init()   
clock = pygame.time.Clock()

game = [0] * 54

mouse = [0, 0, 0]

colors = [[255, 255, 255], [0, 0, 0]]

# Define functions for data processing

def coords_to_index(x, y):
    index = (y * 8) + x
    return index

def index_to_coords(z):
    y = math.floor(z / 8)
    x = z - (y * 8)
    return(x, y)

def piece_color(x):
    if x > 6:
        return(1)
    else:
        return(0)
    

def even_or_odd(x):
    if x % 2 == 0:
        return(0)
    else:
        return(1)

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

    # Print the board before the pieces.
    even_odd = 0
    for i in range(0, 64, 1):
        (x, y) = index_to_coords(i)
        x = 100 + (x * 75)
        y = y * 75
        even_odd = even_or_odd(x + even_or_odd(y))
        if even_odd == 0:
            Texture_White_Tile.texture_draw(x, y)
        else:
            Texture_Black_Tile.texture_draw(x, y)
        pygame.draw.rect(screen, (100, 100, 100), (700, 0, 800, 600))





    pygame.display.update()
    clock.tick(fps)