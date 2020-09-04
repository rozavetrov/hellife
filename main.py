import noise
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# # Constants
WIDTH = 1920
HEIGHT = int(WIDTH/2)
SCALE = 54


# def gaussian(x, mu, sig):
#     return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
#
#
# def rule30(current_state):
#     rule = {
#         "111": 0,
#         "110": 0,
#         "101": 0,
#         "100": 1,
#         "011": 0,
#         "010": 0,
#         "001": 1,
#         "000": 0,
#     }
#
#     return rule[current_state]
#
#
# def get_next_state_of_cell(triplet, rule):
#     return rule(f"{int(triplet[0])}{int(triplet[1])}{int(triplet[2])}")
#
#
# def next_step_cellular_automaton(rule, current_state):
#     return [get_next_state_of_cell(current_state[index:index+3], rule) for index, _ in enumerate(current_state[:-2])]
#
#
# def main():
#     data = np.zeros((TIME, WIDTH))
#
#     data[-1] = np.random.randint(0, 2, WIDTH, dtype=int)
#
#     for index, t in enumerate(range(TIME-1, 0, -1)):
#         new_state_offset = index + 1
#         start_offset = index
#         end_offset = -index
#         if end_offset == 0:
#             end_offset = WIDTH
#
#         next_state = next_step_cellular_automaton(rule30, data[t][start_offset:end_offset])
#         data[t][start_offset:end_offset] = [el*noise.pnoise2(i/SCALE, index/SCALE,
#                                                              octaves=5,
#                                                              persistence=0.1)
#                                             for i, el in enumerate(data[t][start_offset:end_offset])]
#         data[t-1][new_state_offset:-new_state_offset] = next_state
#
#     plt.imsave("figure.png", data)
#
#
# main()

# data = np.array([[gaussian(x, (WIDTH-1)/2, (WIDTH-1)/4)+gaussian(y, (TIME-1)/2, (TIME-1)/4) for x in range(WIDTH)]
#                  for y in range(TIME)])


