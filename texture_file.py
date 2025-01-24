import os
import pygame

screen = pygame.display.set_mode(size=(800,600))

class Texture:
    def __init__(self, image):
        self.image = image
        
    def texture_draw(self, x, y):
        screen.blit(self.image, (x, y))

texture_list = []

texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Pawn.png')))) #0
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Rook.png')))) #1
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Knight.png')))) #2
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Bishop.png')))) #3
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Queen.png')))) #4
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-King.png')))) #5
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Pawn.png')))) #6
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Rook.png')))) #7
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Knight.png')))) #8
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Bishop.png')))) #9
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Queen.png')))) #10
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-King.png')))) #11
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Tile.png')))) #12
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Tile.png')))) #13
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Select-Overlay.png')))) #14
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-White-Icon.png')))) #15
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Black-Icon.png')))) #16
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Log-Outline.png')))) #17
texture_list.append(Texture(pygame.image.load(os.path.join('Textures', 'Chess-Background.png')))) #18