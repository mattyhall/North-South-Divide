import os
from lib.loaddata import DataSet

class PoliceData(DataSet):
    '''
    List of street crimes which are all geolocated
    '''
    
    NAME = 'police'
    BOTTOM = 0.05
    MIDDLE = 0.15
    
    def load(self):
        directory = './data/street_crime/'
        for file in os.listdir(directory):
            handle = open(os.path.join(directory, file), 'r')
            self.load_data(handle)

    def load_data(self, handle):
        line_n = 0
        for line in handle:
            if line_n != 0:
                split = line.split(',')         
                if split[4] and split[5] and split[9]:
                    self.data.append({'longitude': float(split[4]), 'latitude': float(split[5]), 'type': split[9]})
            else:
                line_n += 1

    def get_value(self, row):
        if row['type'] == 'Burglary':
            return 2
        elif row['type'] == 'Robbery':
            return 3
        elif row['type'] == 'Violent crime':
            return 4
        else:
            return  1