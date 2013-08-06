from lib.loaddata import DataSet

class PopulationData(DataSet):
	def load(self):
		file = './data/population.csv'
		handle = open(file, 'r')
		for line in handle:
			split = line.split(',')
			self.data.append([float(split[0]), float(split[1]), float(split[2])])

	def get_value(self, row):
		return row[2]
