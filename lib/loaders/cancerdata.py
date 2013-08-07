from lib.loaddata import DataSet

class CancerData(DataSet):
	NAME = 'cancer'
	BOTTOM = 0.5
	MIDDLE = 0.8
	def load(self):
		handle = open('./data/cancer_survival.csv')
		for row in handle:
			split = row.split(',')
			self.data.append({'latitude': float(split[0]), 'longitude': float(split[1]),
							  'survival_rate': 100 - float(split[2]) + 100- float(split[3]) + 100 - float(split[4])})

	def get_value(self, row):
		return row['survival_rate']