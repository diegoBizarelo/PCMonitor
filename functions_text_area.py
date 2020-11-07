from globals_data import *
from colors import *
from surfaces import text_area_surface


def cpu_info():
    text_area_surface.fill(WHITE)
    cpu_brand = large_ft.render(f"{cpu['brand']}", 1, BLACK)
    cpu_arch = medium_ft.render(f"{cpu['arch']}", 1, BLACK)
    cpu_bits = medium_ft.render(f"{cpu['bits']}", 1, BLACK)
    cpu_frequency = medium_ft.render(f"{round(psutil.cpu_freq(percpu=False).current / 1000, 2)}", 1, BLACK)
    cpu_core = medium_ft.render(f"{psutil.cpu_count(logical=False)}", 1, BLACK)
    cpu_logical = medium_ft.render(f"{psutil.cpu_count(logical=True)}", 1, BLACK)
    height_info = cpu_brand.get_height() + 20
    text_area_surface.blit(cpu_brand, (text_area_surface.get_width() / 2 - cpu_brand.get_width() / 2, 7))
    text_area_surface.blit(small_ft.render(f"Arquitetura: ", 1, GRAY), (30, height_info))
    text_area_surface.blit(cpu_arch, (35, 60))
    text_area_surface.blit(small_ft.render(f"Core(s): ", 1, GRAY), (130, height_info))
    text_area_surface.blit(cpu_core, (140, 60))
    text_area_surface.blit(small_ft.render(f"Logical: ", 1, GRAY), (220, height_info))
    text_area_surface.blit(cpu_logical, (230, 60))
    text_area_surface.blit(small_ft.render(f"Frequency: ", 1, GRAY), (310, height_info))
    text_area_surface.blit(cpu_frequency, (320, 60))
    text_area_surface.blit(small_ft.render(f"Word(bits): ", 1, GRAY), (400, height_info))
    text_area_surface.blit(cpu_bits, (410, 60))
    text_area_surface.blit(small_ft.render(f"Percent: ", 1, GRAY), (490, height_info))
    text_area_surface.blit(medium_ft.render(f"{cpu_line[-1]}%", 1, BLACK), (495, 60))

    core_position = [30, 120]
    for i in range(len(cores_lines[-1])):
        pygame.draw.circle(text_area_surface, colors[i], core_position, 10)
        text_area_surface.blit(small_ft.render(f"Core {i}:", 1, GRAY), (core_position[0] - 15, core_position[1] - 25))
        text_area_surface.blit(small_ft.render(f"% Used:", 1, GRAY), (core_position[0] - 18, core_position[1] + 20))
        text_area_surface.blit(medium_ft.render(f"{cores_lines[-1][i]}%", 1, BLACK),
                               (core_position[0] - 16, core_position[1] + 40))
        core_position[0] += int(text_area_surface.get_width()/8)
        if i/8 == 1 and i > 0:
            core_position[1] += 85
            core_position[0] = 30



def mem_info():
    text_area_surface.fill(WHITE)
    mem_ram = psutil.virtual_memory()
    mem_swap = psutil.swap_memory()
    memory_title = large_ft.render(f"Memory Amount: {round(mem_ram.total / 1024 ** 3, 2)} GB", 1, BLACK)
    swap_tile = large_ft.render(f"Swap Memory: {round(mem_swap.total / 1024 ** 3, 2)} GB", 1, BLACK)
    text_area_surface.blit(memory_title, (text_area_surface.get_width() / 2 - memory_title.get_width() / 2, 7))
    text_area_surface.blit(small_ft.render(f"Used: ", 1, GRAY), (30, memory_title.get_height() + 30))
    text_area_surface.blit(medium_ft.render(f"{round(mem_ram.used / 1024 ** 3, 2)} GB", 1, BLACK), (30, 70))
    text_area_surface.blit(small_ft.render(f"Free: ", 1, GRAY), (170, memory_title.get_height() + 30))
    text_area_surface.blit(medium_ft.render(f"{round(mem_ram.free / 1024 ** 3, 2)} GB", 1, BLACK), (170, 70))
    text_area_surface.blit(small_ft.render(f"Avaliable: ", 1, GRAY), (320, memory_title.get_height() + 30))
    text_area_surface.blit(medium_ft.render(f"{round(mem_ram.available / 1024 ** 3, 2)} GB", 1, BLACK), (320, 70))
    text_area_surface.blit(small_ft.render(f"Percent: ", 1, GRAY), (470, memory_title.get_height() + 30))
    text_area_surface.blit(medium_ft.render(f"{mem_ram.percent} %", 1, BLACK), (470, 70))

    text_area_surface.blit(swap_tile, (text_area_surface.get_width() / 2 - swap_tile.get_width() / 2, 130))
    text_area_surface.blit(small_ft.render(f"Used: ", 1, GRAY), (90, 180))
    text_area_surface.blit(medium_ft.render(f"{round(mem_swap.used / 1024 ** 3, 2)} GB", 1, BLACK), (90, 200))
    text_area_surface.blit(small_ft.render(f"Free: ", 1, GRAY), (230, 180))
    text_area_surface.blit(medium_ft.render(f"{round(mem_swap.free / 1024 ** 3, 2)} GB", 1, BLACK), (230, 200))
    text_area_surface.blit(small_ft.render(f"Percent: ", 1, GRAY), (380, 180))
    text_area_surface.blit(medium_ft.render(f"{mem_swap.percent} %", 1, BLACK), (380, 200))


def discs_info():
    discs = list(map(lambda disk: disk.device, psutil.disk_partitions(all=True)))
    d = psutil.disk_io_counters(perdisk=True, nowrap=True)

    text_area_surface.fill(WHITE)
    title = large_ft.render(f"Discs", 1, BLACK)
    text_area_surface.blit(title, (text_area_surface.get_width() / 2 - title.get_width() / 2, 7))
    titles = {'x': 20, 'y': title.get_height() + 15}
    space = (text_area_surface.get_width() - 20) / len(discs)
    for k in discs:
        try:
            disc = psutil.disk_usage(k)
        except FileNotFoundError:
            continue

        text_area_surface.blit(medium_ft.render(k, 1, BLACK), (titles['x'], titles['y']))
        t = small_ft.render(f"Total: ", 1, GRAY)
        text_area_surface.blit(t, (titles['x'], titles['y'] + 30))
        text_area_surface.blit(medium_ft.render(f"{round(disc.total / 1024 ** 3, 2)} GB", 1, BLACK),
                               (titles['x'], titles['y'] + t.get_height() + 35))
        text_area_surface.blit(small_ft.render(f"Free: ", 1, GRAY), (titles['x'], titles['y'] + 75))
        text_area_surface.blit(medium_ft.render(f"{round(disc.free / 1024 ** 3, 2)} GB", 1, BLACK),
                               (titles['x'], titles['y'] + 90))
        text_area_surface.blit(small_ft.render(f"Used: ", 1, GRAY), (titles['x'], titles['y'] + 120))
        text_area_surface.blit(medium_ft.render(f"{round(disc.used / 1024 ** 3, 2)} GB", 1, BLACK),
                               (titles['x'], titles['y'] + 135))
        text_area_surface.blit(small_ft.render(f"% Used: ", 1, GRAY), (titles['x'], titles['y'] + 165))
        text_area_surface.blit(medium_ft.render(f"{disc.percent}%", 1, BLACK),
                               (titles['x'], titles['y'] + 180))
        titles['x'] += space


PC_INFO = {'CPU': cpu_info, 'MEM': mem_info, 'DISC': discs_info}

