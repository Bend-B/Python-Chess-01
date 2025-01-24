import pygame
pygame.font.init()

ui_font = pygame.font.SysFont("Arial", 15)

from texture_file import texture_list

def render_ui(turn, log):
    texture_list[18].texture_draw(600, 0)


    if turn == 1:
        texture_list[15].texture_draw(640, 80)
    else:
        texture_list[16].texture_draw(640, 80)

    texture_list[17].texture_draw(640, 240)

    text_surfaces = []

    for item in log:
        string = item[0]+" - "+item[1]
        text_surfaces.append(ui_font.render(string, False, (255, 255, 255)))


    return text_surfaces
