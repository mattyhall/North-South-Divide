class DataSet(object):
    '''
    All data loaders should inherit from this class. Each of the methods and variables here should be
    implemented. 
    '''
    NAME = ''
    BOTTOM = 0.1
    MIDDLE = 0.8    

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