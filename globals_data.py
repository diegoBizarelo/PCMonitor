import cpuinfo
import psutil
import time
import pygame
from colors import *

cpu = cpuinfo.get_cpu_info()
mem = psutil.virtual_memory()

pygame.font.init()
font = pygame.font.SysFont('Calibri', 15)
small_ft = pygame.font.SysFont('Calibri', 12)
medium_ft = pygame.font.SysFont('Calibri', 16)
large_ft = pygame.font.SysFont('Calibri', 24)

graph_cicle = 50
cpu_line = [0] * graph_cicle
mem_line = [0] * graph_cicle
cores_lines = [[0 for i in range(len(psutil.cpu_percent(percpu=True)))] for i in range(graph_cicle)]

count = 0
run = True
click_area = {}

time_delay = time.time() + 1
rectangle_graph = {'h': 101, 'w': 151}

key = 'CPU'

colors = [BLUE, PURPLE, GREEN, YELLOW, BROWN, RED, ORANGE, D_GREEN, TEAL, LIME, MAROON, SILVER,
             NAVY, MAGENTA, INDIGO, ROSBROWN, CHOC, AQUA]
