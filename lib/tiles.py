def build_tiles(data_set, step, top, bottom, left, right):
    # top - bottom here gives the number of degrees that our data covers
    # dividing by step gives the number of areas it will be split into but is off by one
    tiles = [[0 for y in xrange(1 + int((top - bottom) / step))] for x in range(1 + int((right - left) / step))]
    for row in data_set:
        # find the tile it is in and increase the count by whatever the data set returns
        tile_lat = int((row['latitude'] - bottom) / step) 
        tile_long = int((row['longitude'] - left) / step)
        tiles[tile_long][tile_lat] += data_set.get_value(row)
    return tiles

def normalise_tiles(tiles):
    flat = []
    maximum = -1
    minimum = 10000000
    for column in tiles:
        for tile in column:
            if tile > maximum:
                maximum = tile
            if tile < minimum:
                minimum = tile

    for x in range(len(tiles)):
        for y in range(len(tiles[x])):
            tiles[x][y] = (tiles[x][y] - minimum) / float(maximum - minimum)
    return tiles