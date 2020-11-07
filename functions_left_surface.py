from globals_data import *
from surfaces import *
import clickable


def add_clickable_area(surface, component, pos):
    click_area[component] = []
    click_area[component].append(surface)
    click_area[component].append(clickable.Clickable(((pos[0], pos[1]),
                                                      (pos[0] + surface.get_size()[0],
                                                       pos[1] + surface.get_size()[1]))))


def draw_line(surface, line_coord, rectangle, margin, component, percent, pos):
    surface.fill(WHITE)
    left_surface.fill(WHITE)
    COLOR = {'MEM': PURPLE, 'CPU': BLUE}
    r = pygame.draw.rect(surface, COLOR[component], (margin, margin, rectangle[0], rectangle[1]), 2)
    if component not in click_area: add_clickable_area(surface, component, pos)

    # texts
    surface.blit(font.render('0', 1, BLACK), (rectangle[0] + margin, rectangle[1] + margin))
    surface.blit(font.render('100%', 1, BLACK), (rectangle[0] + margin, int(margin / 1.5)))
    surface.blit(font.render(component, 1, BLACK), (5, int(surface.get_height()/2 - 10)))
    surface.blit(font.render(str(int(percent)) + "%", 1, BLACK), (5, int(surface.get_height()/2 + 5)))

    floor = r.size[1] + margin - 1
    line = r.size[0] + margin - 1
    p = (r.size[0] - 1) / graph_cicle

    last = line_coord[-1]
    for i in range(len(line_coord), 0, -1):
        pygame.draw.aaline(surface, COLOR[component], (line, floor - last), (line - p, floor - line_coord[i - 1]), 1)
        line -= p
        last = line_coord[i - 1]


def show_discs_info(surface, discs):
    surface.fill(WHITE)
    text = large_ft.render('DISCS:', 1, BLACK)
    text_count = [25, 7 + text.get_size()[1]]
    rect_count = [25, 23 + text.get_size()[1]]
    surface.blit(text, (int(surface.get_size()[0] / 2 - text.get_size()[0] / 2), 5))

    for key in discs:
        try:
            disc = psutil.disk_usage(key)
        except FileNotFoundError:
            continue
        larg = surface.get_size()[0] / 1.5
        used = larg * disc.percent / 100
        color = OLIVE if disc.percent < 90 else RED
        rect = pygame.draw.rect(surface, GREEN, (rect_count[0], rect_count[1], int(larg), 10))
        pygame.draw.rect(surface, color, (rect_count[0], rect_count[1], int(used), 10))
        surface.blit(font.render(str(disc.percent) + '%', 10, BLACK),
                     (rect.size[0] + rect_count[0] + 5, rect_count[1] - 3))
        surface.blit(font.render(key, 1, BLACK), text_count)

        text_count[1] += 30
        rect_count[1] += 30


