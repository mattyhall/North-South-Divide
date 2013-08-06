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
            if row['latitude'] > max_lat:
                max_lat = row['latitude']
            elif row['latitude'] < min_lat:
                min_lat = row['latitude']
            if row['longitude'] > max_long:
                max_long = row['longitude']
            elif row['longitude'] < min_long:
                min_long = row['longitude']
        return min_lat, max_lat, min_long, max_long

    def __iter__(self):
        return iter(self.data)