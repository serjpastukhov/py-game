import os
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    
    image = image.convert_alpha()

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    return image