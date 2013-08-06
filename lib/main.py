from lib.loaddata import *
from lib.tiles import *

def do_all_of_it_terrible_function_name_im_so_sorry_forgive_me():
    directory = './data/street_crime/'
    data = load_all_data_in_directory(directory)
    bottom, top, left, right = min_max_lat_long(data)
    # the step is how far up the country will it move each time (in degrees)
    step = 0.2
    tiles = build_tiles(data, step, top, bottom, left, right)
    print tiles    
    normalise_tiles(tiles)
    draw_data = {'lines': []}
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
        draw_data['lines'].append([latitude, longitude])
        draw_data['lines'].append([latitude + step, longitude + step])
    return draw_data