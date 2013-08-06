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