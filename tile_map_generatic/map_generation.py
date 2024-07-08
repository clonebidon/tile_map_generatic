import random

def generate(num_tiles):
    tiles = []
    for y in range(num_tiles[0]):
        tiles.append([])
        for x in range(num_tiles[1]):
            rand = random.randint(0, 2)
            if rand == 0:
                tiles[y].append(0)
            elif rand == 1:
                tiles[y].append(2)
            else:
                tiles[y].append(1)

    return tiles