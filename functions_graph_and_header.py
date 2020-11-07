from globals_data import *
from surfaces import *
import math


def text_info_view(surface, k):
    surface.fill(WHITE)
    net_it = psutil.net_if_addrs()
    ip = net_it['Ethernet'][1].address
    text = large_ft.render(f"← {k} →", 1, BLACK)
    text_ip = large_ft.render(f"IP: {ip}", 1, BLACK)
    surface.blit(text, (int(surface.get_size()[0] / 2 - text.get_size()[0] / 2), 0))
    surface.blit(text_ip, (5, 2))


def draw_lines_cores(surface, cpu_cores, floor, rect_length, line_length, rect):
    last = cpu_cores[-1]
    for i in range(len(cpu_cores) - 1, 0, -1):
        for v in range(len(cpu_cores[i])):
            pygame.draw.aaline(surface, colors[v], (rect_length, floor - ((rect.size[1] / 100) * last[v])),
                               (rect_length - line_length, floor - ((rect.size[1] / 100) * cores_lines[i][v])), 1)
        rect_length -= line_length
        last = cores_lines[i]


def draw_line_mem(surface, mem_info, floor, rect_length, line_length, rect):
    last_coord = mem_info[-1]
    for i in range(len(mem_info), 0, -1):
        pygame.draw.aaline(surface, PURPLE, (rect_length, int(floor - ((rect.size[1] / 100) * last_coord))),
                           (rect_length - line_length, int(floor - ((rect.size[1] / 100) * mem_info[i-1]))), 1)
        rect_length -= line_length - 0.23
        last_coord = mem_info[i - 1]


def draw_discs(surface, discs, floor, rect_length, line_length, rect):
    h_line_pos = rect.size[0]/3

    for k in discs.keys():
        pygame.draw.line(surface, BLACK, (h_line_pos, floor), (h_line_pos, floor - rect.size[1] + 2))
        h_line_pos += h_line_pos


def draw_graph_rectangle(line_coord, component, footer_msg):
    graph_surface.fill(WHITE)

    margin = 30
    pos = [15, 15]
    rect = pygame.draw.rect(graph_surface, BLACK, (5, pos[1], 541, 251), 1)
    graph_surface.blit(font.render(component, 1, GRAY), (5, 0))
    graph_surface.blit(small_ft.render(footer_msg, 1, GRAY), (5, graph_surface.get_height() - 15))

    floor = rect.size[1] + margin / 2 - 1
    h = rect.size[0] + 3
    p = math.ceil(rect.size[0] / graph_cicle)

    draw = {'CPU': draw_lines_cores, 'MEM': draw_line_mem, 'DISC': draw_discs}
    draw[component](graph_surface, line_coord, floor, h, p, rect)


