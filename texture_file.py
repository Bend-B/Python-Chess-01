import os
import pygame

screen = pygame.display.set_mode(size=(800,600))

class Texture:
    def __init__(self, image):
        self.image = image
        
    def texture_draw(self, x, y):
        screen.blit(self.image, (x, y))

texture_list = []

texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Pawn.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Rook.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Knight.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Bishop.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Queen.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-King.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Pawn.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Rook.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Knight.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Bishop.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Queen.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-King.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Tile.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Tile.png'))))
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Select-Overlay.png'))))