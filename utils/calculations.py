from bisect import bisect_right
from random import random

DISCORD_EPOCH = 1420070400000

def snowflake_to_time(id):
    return (id >> 22) + DISCORD_EPOCH

def time_difference(id1, id2):
    return abs(snowflake_to_time(id1) - snowflake_to_time(id2)) / 1000

def generate_slot_grid(items, weights):

    slot_grid = []

    for i in range(3):

        row = []

        for j in range(5):
            row.append(items[bisect_right(weights, random())])

        slot_grid.append(row)

    return slot_grid