import numpy as np
from array2gif import write_gif
import time


class World:
    def __init__(self, width, height, time):
        self.map = np.zeros((time, height, width), dtype="uint8")
        self.rgb_map = np.zeros((time, height, width, 3), dtype="uint8")
        self.current_time = 0
        self.states = np.array([[0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0]])
        self.rgb_array_white = np.array([255, 255, 255])
        self.rgb_array_black = np.array([0, 0, 0])

    @property
    def width(self):
        return self.map.shape[2]

    @property
    def height(self):
        return self.map.shape[1]

    @property
    def time(self):
        return self.map.shape[0]

    def get_neighbours_of_cell(self, x, y):
        return self.map[self.current_time, y - 1:y + 2, x - 1:x + 2]

    def set_initial_state(self, prob=(0.5, 0.5), seed=None):
        if seed:
            np.random.seed(seed)

        self.map[0] = np.random.choice((0, 1), (self.height, self.width), p=prob)

    def get_new_state_of_cell(self, x, y):
        neighbours = self.get_neighbours_of_cell(x, y)

        return self.rule(neighbours)

    def create(self):
        for t in range(self.time - 1):
            self.current_time = t

            for y in range(1, self.height - 1):
                for x in range(1, self.width - 1):
                    self.map[self.current_time + 1][y][x] = self.get_new_state_of_cell(x, y)
                    self.rgb_map[self.current_time + 1][y][x] = self.rgb_array_white if self.map[self.current_time + 1][y][x] else self.rgb_array_black

            self.current_time += 1

        self.current_time = 0

    def to_rgb(self):
        for t in range(self.time):
            for y in range(self.height):
                for x in range(self.width):
                    self.rgb_map[t, y, x] = np.array([255, 255, 255]) * self.map[t, y, x]

        return self.rgb_map

    def rule(self, cells):
        main_cell = cells[1][1]
        count_of_alive = cells[0][0] + cells[0][1] + cells[0][2] + cells[1][0] + cells[1][2] + cells[2][0] + cells[2][1] + cells[2][2]

        return self.states[main_cell][count_of_alive]

    def write_to_gif(self, filename, folder_path, fps=10):
        write_gif(self.rgb_map, f"{folder_path}/{filename}", fps=fps)


if __name__ == '__main__':
    WIDTH = 100
    HEIGHT = 100
    TIME = 50

    start = time.time()
    world = World(WIDTH, HEIGHT, TIME)

    world.set_initial_state(prob=(0.9, 0.1))
    world.create()

    end = time.time() - start

    world.write_to_gif(f"test.gif", "./maps", fps=30)
    time_to_gif = time.time() - start

    print(end, time_to_gif)
