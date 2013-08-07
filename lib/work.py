from lib.loaddata import *
from lib.tiles import *

def work(data_set):
    bottom, top, left, right = data_set.min_max_lat_long()
    # the step is how far up the country will it move each time (in degrees)
    step = 0.2
    tiles = build_tiles(data_set, step, top, bottom, left, right)
    tiles = normalise_tiles(tiles)
    draw_data = {'squigle_line': [], 'circles': []}
    for x in range(len(tiles)):
        max_difference = latitude = -1
        tile = tiles[x]
        longitude = left + step * x
        for y in range(len(tile)):
            # the south is defined as the tiles less than and including y, the north is the ones above
            south = tile[0:y+1]
            north = tile[y:]
            south_count = sum(south)
            north_count = sum(north)
            # we divide by the number of tiles to get an average taking into account area
            south_count /= len(south)
            north_count /= len(north)
            diff = abs(north_count - south_count)
            # if it is the biggest difference between north and south we store it for later
            if diff > max_difference and north_count != 0 and south_count != 0:
                max_difference = diff
                latitude = bottom + step * y
            # assign a colour based on how many data points there were - red lots, amber some, green very little
            colour = '#FF0000'
            # the bands may be different per data set (eg what value is green) so we put that in the data set's class
            if 0 < tile[y] < data_set.BOTTOM:
                colour = '#00FF00'
            elif data_set.BOTTOM <= tile[y] < data_set.MIDDLE:
                # amber
                colour = '#FF9900'
            # we check if the latitude is more than 0. There were weird bugs where a line would be drawn to the equator
            if tile[y] > 0:
                # intensity is 
                draw_data['circles'].append({'latitude': bottom + step * y + step / 2, 
                                             'longitude': longitude + step / 2, 
                                             'colour': colour, 
                                             'intensity': tile[y]})
        if latitude >= 40:
            draw_data['squigle_line'].append({'latitude': latitude, 'longitude': longitude})
            draw_data['squigle_line'].append({'latitude': latitude, 'longitude': longitude + step})
    # to take an average we need to find the area underneath the line
    area = 0
    for point in xrange(0, len(draw_data['squigle_line']), 2):
        # we make a trapezium out of this data point and the next one
        a = draw_data['squigle_line'][point]['latitude'] - bottom
        b = draw_data['squigle_line'][point]['latitude'] - bottom
        # and find the area
        area += ((a + b) * step) / 2.0
    # to get a straight, horizontal line we can treat the area as a rectangle
    height = area / abs(right - left) + bottom
    draw_data['average_line'] = [{'latitude': height, 'longitude': left}, {'latitude': height, 'longitude': right}]
    return draw_data
