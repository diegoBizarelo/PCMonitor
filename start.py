import sys
from pygame.locals import *
from functions_text_area import PC_INFO
from functions_left_surface import *
from functions_graph_and_header import *

# Config pygame
clock = pygame.time.Clock()
pygame.display.set_caption("Graph")

click_area: add_clickable_area(discs_surface, 'DISC', (0, cpu_surface.get_size()[1] * 2))
text_info_view(header_surface, 'CPU')


def fill_surfaces():
    left_surface.blit(cpu_surface, (0, 0))
    left_surface.blit(mem_surface, (0, cpu_surface.get_height()))
    left_surface.blit(discs_surface, (0, cpu_surface.get_height() * 2))
    information_surface.blit(graph_surface, (0, header_surface.get_height()))
    information_surface.blit(header_surface, (0, 0))
    information_surface.blit(text_area_surface, (0, graph_surface.get_height() + header_surface.get_height()))
    screen.blit(left_surface, (0, 0))
    screen.blit(information_surface, (left_surface.get_width(), 0))


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_button = pygame.mouse.get_pressed()
            if mouse_button[0]:
                for c in click_area:
                    if click_area[c][1].in_range(pos):
                        key = c
                        count = list(PC_INFO.keys()).index(key)
                        text_info_view(header_surface, key)

        if event.type == pygame.KEYDOWN:
            k = pygame.key.get_pressed()
            if k[K_LEFT]:
                count -= 1
            elif k[K_RIGHT]:
                count += 1
            key = list(PC_INFO.keys())[count % len(PC_INFO)]
            text_info_view(header_surface, key)

    if time.time() > time_delay:
        cpu_line.pop(0)
        cpu_line.append(psutil.cpu_percent(percpu=False))

        mem_line.pop(0)
        mem_line.append(psutil.virtual_memory().percent)

        cores_lines.pop(0)
        cores_lines.append(psutil.cpu_percent(percpu=True))

        if key == 'CPU':
            draw_graph_rectangle(cores_lines, 'CPU', f"{graph_cicle} seconds")
        elif key == 'MEM':
            draw_graph_rectangle(mem_line, 'MEM', f"{graph_cicle} seconds")
        elif key == 'DISC':
            draw_graph_rectangle(psutil.disk_io_counters(perdisk=True, nowrap=True), 'DISC', f"Physical Discs")

        draw_line(cpu_surface, cpu_line, (rectangle_graph['w'],
                                          rectangle_graph['h']), 40, 'CPU', cpu_line[-1], (0, 25))

        draw_line(mem_surface, mem_line, (rectangle_graph['w'],
                                          rectangle_graph['h']), 40, 'MEM', mem_line[-1], (0, 175))

        show_discs_info(discs_surface, list(map(lambda disk: disk.device, psutil.disk_partitions(all=True))))

        time_delay = time.time() + 1

    PC_INFO[key]()
    fill_surfaces()
    pygame.display.flip()
    # 60 frames por segundo
    clock.tick(60)

pygame.quit()
sys.exit()
