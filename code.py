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

def main():
    # directory = 'test_data'
    directory = './street_crime/'
    data = load_all_data_in_directory(directory)
    bottom, top = min_max_lat(data)
    max_difference = -1
    latitude = 0
    step = 0.2
    i = 0
    for lat in drange(bottom+step, top, step):
        south_count = north_count = 0
        for row in data:
            if bottom <= row[1] <= lat:
                south_count += 1
            elif lat < row[1] < top:
                north_count += 1
        south_count /= (lat - bottom) / step
        north_count /= (top - lat) / step
        diff = abs(north_count - south_count)
        # print lat, diff
        if diff > max_difference and north_count != 0 and south_count != 0:
         max_difference = diff
         latitude = lat
    print bottom, top
    print 'Answer!', latitude

if __name__ == '__main__':
    main()
