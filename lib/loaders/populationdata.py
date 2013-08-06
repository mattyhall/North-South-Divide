from lib.loaddata import DataSet

class PopulationData(DataSet):
    BOTTOM = 0.2
    MIDDLE = 0.5

    def load(self):
        file = './data/population.csv'
        handle = open(file, 'r')
        for line in handle:
            split = line.split(',')
            self.data.append({'longitude': float(split[0]), 'latitude': float(split[1]), 'population': float(split[2])})

    def get_value(self, row):
        return row['population']
