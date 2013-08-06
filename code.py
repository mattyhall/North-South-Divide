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

def min_max_lat_long(data):
    min_lat = min_long = 10000000
    max_lat = max_long = -1
    for row in data:
        if row[1] > max_lat:
            max_lat = row[1]
        elif row[1] < min_lat:
            min_lat = row[1]
        if row[0] > max_long:
            max_long = row[0]
        elif row[0] < min_long:
            min_long = row[0]
    return min_lat, max_lat, min_long, max_long

def build_tiles(data, step, top, bottom, left, right):
    # top - bottom here gives the number of degrees that our data covers
    # dividing by step gives the number of areas it will be split into but is off by one
    tiles = [[0 for y in xrange(1 + int((top - bottom) / step))] for x in range(1 + int((right - left) / step))]
    for row in data:
        # find the tile it is in and increase the crime count by one
        tile_lat = int((row[1] - bottom) / step) 
        tile_long = int((row[0] - left) / step)
        tiles[tile_long][tile_lat] += 1
    return tiles

def main():
    directory = './street_crime/'
    data = load_all_data_in_directory(directory)
    bottom, top, left, right = min_max_lat_long(data)
    # the step is how far up the country will it move each time (in degrees)
    step = 0.2
    tiles = build_tiles(data, step, top, bottom, left, right)
    for x in range(len(tiles)):
        max_difference = latitude = -1
        tile = tiles[x]
        longitude = left + step * x
        for y in range(len(tiles)):
            # the south is defined as the tiles less that and including y, the north is the ones above
            south = tile[0:y+1]
            north = tile[y:]
            south_count = sum(south)
            north_count = sum(north)
            # we divide by the number of tiles to get an average taking into account area
            south_count /= len(south)
            north_count /= len(north)
            diff = abs(north_count - south_count)
            if diff > max_difference and north_count != 0 and south_count != 0:
             max_difference = diff
             latitude = bottom + step * y
        print 'new google.maps.LatLng(' + str(latitude) + ',' + str(longitude) + '),'
        print 'new google.maps.LatLng(' + str(latitude+step) + ',' + str(longitude+step) + '),'

if __name__ == '__main__':
    main()
