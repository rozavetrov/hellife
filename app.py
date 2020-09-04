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
        self.barrier = None

    @property
    def width(self):
        return self.map.shape[2]

    @property
    def height(self):
        return self.map.shape[1]

    @property
    def time(self):
        return self.map.shape[0]

    def get_neighbours_of_cell(self, x, y, t):
        return self.map[t, y - 1:y + 2, x - 1:x + 2]

    def set_initial_state(self, prob=(0.5, 0.5), seed=None):
        if seed:
            np.random.seed(seed)

        self.map[0] = np.random.choice((0, 1), (self.height, self.width), p=prob)

    def get_new_state_of_cell(self, x, y, t):
        neighbours = self.get_neighbours_of_cell(x, y, t)

        return self.rule(neighbours)

    def set_new_state(self, map_chunk):
        for t in range(self.time - 1):
            for y in range(1, map_chunk.shape[1] - 1):
                for x in range(1, map_chunk.shape[2] - 1):
                    map_chunk[t + 1][y][x] = self.get_new_state_of_cell(x, y, t)
                    # self.rgb_map[t + 1][y][x] = self.rgb_array_white \
                    #     if self.map[t + 1][y][x] else self.rgb_array_black

    def get_map_chunk(self, start_h, end_h, start_w, end_w):
        return self.map[:][start_h:end_h][start_w:end_w]

    def get_map_chunks(self, chunk_height, chunk_width):
        chunks = []
        step_w = int(self.width/chunk_width)
        step_h = int(self.height/chunk_height)

        start_h = 0
        start_w = 0
        while start_h < self.height:
            end_h = start_h + step_h
            while start_w < self.width:
                end_w = start_w + step_w
                chunks.append(self.get_map_chunk(start_h, end_h, start_w, end_w))

                start_w += step_w
            start_h += step_h

        return chunks

    def rule(self, cells):
        main_cell = cells[1][1]
        count_of_alive = cells[0][0] + cells[0][1] + cells[0][2] + cells[1][0] + cells[1][2] + cells[2][0] + cells[2][1] + cells[2][2]

        return self.states[main_cell][count_of_alive]


if __name__ == '__main__':
    WIDTH = 160
    HEIGHT = 100
    TIME = 200

    start = time.time()
    world = World(WIDTH, HEIGHT, TIME)

    world.set_initial_state(prob=(0.9, 0.1))

    map_chunks = world.get_map_chunks(HEIGHT, WIDTH/8)
    for chunk in map_chunks:
        world.set_new_state(chunk)

    end = time.time() - start

    write_gif(world.rgb_map, f"./maps/test.gif", fps=10)
    time_to_gif = time.time() - start

    print(end, time_to_gif)
