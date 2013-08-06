import os

class DataSet(object):
    def __init__(self):
        self.data = []

    def load(self):
        pass

    def get_value(self, row):
        pass

    def min_max_lat_long(self):
        min_lat = min_long = 10000000
        max_lat = max_long = -1
        for row in self.data:
            if row[1] > max_lat:
                max_lat = row[1]
            elif row[1] < min_lat:
                min_lat = row[1]
            if row[0] > max_long:
                max_long = row[0]
            elif row[0] < min_long:
                min_long = row[0]
        return min_lat, max_lat, min_long, max_long

    def min_max_lat_long(self):
        min_lat = min_long = 10000000
        max_lat = max_long = -1
        for row in self.data:
            if row[1] > max_lat:
                max_lat = row[1]
            elif row[1] < min_lat:
                min_lat = row[1]
            if row[0] > max_long:
                max_long = row[0]
            elif row[0] < min_long:
                min_long = row[0]
        return min_lat, max_lat, min_long, max_long

    def __iter__(self):
        return iter(self.data)

class PoliceData(DataSet):
    def load(self, directory):
        for file in os.listdir(directory):
            handle = open(os.path.join(directory, file), 'r')
            self.load_data(handle)

    def load_data(self, handle):
        line_n = 0
        for line in handle:
            if line_n != 0:
                split = line.split(',')         
                if split[4] and split[5] and split[9]:
                    self.data.append([float(split[4]), float(split[5]), split[9]])
            else:
                line_n += 1

    def get_value(self, row):
        if row[2] == 'Burglary':
            return 2
        elif row[2] == 'Robbery':
            return 3
        elif row[2] == 'Violent crime':
            return 4
        else:
            return  1