import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def get_neighbours(cell, colony):
    # Кортеж смещений координат смежных ячеек
    dxdy = ((1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0))
    # Пары координат 8 смежных ячеек
    nearest_pairs = [(cell[0] + dx, cell[1] + dy) for dx, dy in dxdy]
    # Оставляет только те из них, которые заняты живыми клетками
    neighbours = set(filter(lambda c: c in colony, nearest_pairs))
    return neighbours


def get_areal(colony):
    dxdy = [(1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)]
    areal = set([(cell[0] + dx, cell[1] + dy) for dx, dy in dxdy for cell in colony])
    return areal.difference(colony)


def next_generation(colony):
    # Рождающиеся клетки (клетка из ареала колонии с 3 соседями)
    born = set(filter(lambda c: len(get_neighbours(c, colony)) == 3, get_areal(colony)))
    # Клетка переходящая в следующее поколение (2 или 3 соседа)
    live = set(filter(lambda c: len(get_neighbours(c, colony)) in (2, 3), colony))
    # Объединяем рождающиеся клетки с выжившими клетками в одно множество
    next_generation = born.union(live)
    return next_generation


colony = {(2, 2), (3, 2), (4, 2), (4, 3), (3, 4)}
for i in range(0, 100):
    print(i)
    fig, ax = plt.subplots(figsize=[3, 3])
    [ax.add_patch(Rectangle((x, y), 1, 1)) for x, y in colony]
    plt.xlim([-20, 20])
    plt.ylim([-20, 20])
    plt.grid(ls=':')
    plt.show()
    colony = next_generation(colony)
    print(colony)
    time.sleep(1)
