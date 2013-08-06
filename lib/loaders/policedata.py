import os
from lib.loaddata import DataSet

class PoliceData(DataSet):
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