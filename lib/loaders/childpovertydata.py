from lib.loaddata import DataSet

class ChildPovertyData(DataSet):
    '''
    Percentage of children in poverty per lat/lng
    '''
    NAME = 'childpoverty'
    BOTTOM = 0.1
    MIDDLE = 0.45  

    def load(self):
        handle = open('./data/child_poverty.csv')
        for row in handle:
            row = row.strip()
            split = row.split(',')
            print(split)
            if len(split) == 3:
                self.data.append({'latitude': float(split[1]), 'longitude': float(split[0]), 'percentage': float(split[2])})

    def get_value(self, row):
        return row['percentage']
