# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import config

def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_rectangle(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))

def new_textbox(font, text, height, color=(0, 0, 0)):
    text_surface = font.render(text, True, color)
    text_width = text_surface.get_width()
    text_x = (config.WINDOW_WIDTH - text_width) // 2
    return {
        'text surface' : text_surface,
        'pos' : [text_x, height]
        }

def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 36)

    rect_1 = {
        'color' : config.RED,
        'pos' : [95, 325],
        'width' : 250,
        'height' : 125,
        'speed' : 1
    }
    rect_2 = {
        'color' : (0, 255, 100),
        'pos' : [300, 100],
        'width' : 100,
        'height' : 100,
        'speed' : 2
    }

    textbox1 = new_textbox(font, 'Hello, Pygame!', 50, color=config.BLUE)
    textbox2 = new_textbox(font, '*Pygame waves back.*', 550)
    while running:
        running = handle_events() # Events & movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect_1['pos'][0] -= rect_1['speed']
        if keys[pygame.K_RIGHT]:
            rect_1['pos'][0] += rect_1['speed']
        if keys[pygame.K_UP]:
            rect_1['pos'][1] -= rect_1['speed']
        if keys[pygame.K_DOWN]:
            rect_1['pos'][1] += rect_1['speed']
        
        if keys[pygame.K_a]:
            rect_2['pos'][0] -= rect_2['speed']
        if keys[pygame.K_d]:
            rect_2['pos'][0] += rect_2['speed']
        if keys[pygame.K_w]:
            rect_2['pos'][1] -= rect_2['speed']
        if keys[pygame.K_s]:
            rect_2['pos'][1] += rect_2['speed']

        screen.fill(config.WHITE) # Begin Drawing

        draw_rectangle(screen, rect_1['color'], rect_1['pos'][0], rect_1['pos'][1], rect_1['width'], rect_1['height'])
        draw_rectangle(screen, rect_2['color'], rect_2['pos'][0], rect_2['pos'][1], rect_2['width'], rect_2['height'])
        
        screen.blit(textbox1['text surface'], textbox1['pos'])
        screen.blit(textbox2['text surface'], textbox2['pos'])
        pygame.display.flip()
        # Limit clock to FPS
        clock.tick(config.FPS)
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()