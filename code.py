import os

def load_data(data, handle):
    line_n = 0
    for line in handle:
        if line_n != 0:
            split = line.split(',')         
            if split[4] and split[5] and split[9]:
                data.append([float(split[4]), float(split[5]), split[9]])
        else:
            line_n += 1

def load_all_data_in_directory(dir):
    data = []
    for file in os.listdir(dir):
        handle = open(os.path.join(dir, file), 'r')
        load_data(data, handle)
    return data

def drange(first, last, step):
    x = first
    while x <= last:
        yield x
        x += step

def min_max_lat(data):
    min_lat = 10000000
    max_lat = -1
    for row in data:
        if row[1] > max_lat:
            max_lat = row[1]
        elif row[1] < min_lat:
            min_lat = row[1]
    return min_lat, max_lat

def build_tiles(data, step, top, bottom):
    # top - bottom here gives the number of degrees that our data covers
    # dividing by step gives the number of areas it will be split into but is off by one
    tiles = [0 for x in range(1 + int((top - bottom) / step))]
    for row in data:
        # find the tile it is in and increase the crime count by one
        tile_lat = int((row[1] - bottom) / step) 
        tiles[tile_lat] += 1
    return tiles

def main():
    directory = './street_crime/'
    data = load_all_data_in_directory(directory)
    bottom, top = min_max_lat(data)
    # the step is how far up the country will it move each time (in degrees)
    step = 0.2
    tiles = build_tiles(data, step, top, bottom)
    max_difference = latitude = -1
    for i in range(len(tiles)):
        # the south is defined as the tiles less that and including i, the north is the ones above
        south = tiles[0:i+1]
        north = tiles[i:]
        south_count = sum(south)
        north_count = sum(north)
        # we divide by the number of tiles to get an average taking into account area
        south_count /= len(south)
        north_count /= len(north)
        diff = abs(north_count - south_count)
        if diff > max_difference and north_count != 0 and south_count != 0:
         max_difference = diff
         latitude = bottom + step * i
    print 'Answer!', latitude

if __name__ == '__main__':
    main()
