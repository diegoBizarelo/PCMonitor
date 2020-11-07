import pygame
from colors import *

size = {'x': 800, 'y':600}

#Surfaces
screen = pygame.display.set_mode((size['x'], size['y']))
screen.fill(WHITE)

header_surface = pygame.surface.Surface((550, 30))
header_surface.fill(WHITE)

left_surface = pygame.surface.Surface((250, 600))
left_surface.fill(WHITE)

information_surface = pygame.surface.Surface((550, 600))
information_surface.fill(WHITE)

graph_surface = pygame.surface.Surface((information_surface.get_width(),
                                        information_surface.get_height()/2 - header_surface.get_height()/2))
graph_surface.fill(WHITE)

text_area_surface = pygame.surface.Surface((information_surface.get_width(),
                                            information_surface.get_height()/2 - header_surface.get_height()/2))
text_area_surface.fill(WHITE)

cpu_surface = pygame.surface.Surface((250, 160))
cpu_surface.fill(WHITE)

mem_surface = pygame.surface.Surface((250, 160))
mem_surface.fill(WHITE)

# cores_surface = pygame.surface.Surface((525, 225))
# cores_surface.fill(PURPLE)

discs_surface = pygame.surface.Surface((left_surface.get_size()[0],
                                        left_surface.get_size()[1] - cpu_surface.get_size()[1]*2 - 10))
discs_surface.fill(WHITE)
