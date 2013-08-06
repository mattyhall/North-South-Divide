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