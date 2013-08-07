import os
from postcodes import PostCoder

pc = PostCoder()

def postcode_to_coords(n):  #Find coordinates from postcode
	result = pc.get(n)
	if result is None:
		return None, None	
	result = result['geo']
	latitude = result['lat']
	longitude = result['lng']
	return latitude, longitude

for file in os.listdir('.'):
	if file.endswith('.csv'):
		handle = open(file, 'r')
		data = ''
		latitude = longitude = price = 0
		for row in handle:
			split = row.split(',')
			price = split[1]
			postcode = split[3]
			latitude, longitude = postcode_to_coords(postcode)
			print price, latitude, longitude
			if (not latitude is None) and (not longitude is None) and (not price is None):
				data += price + ',' + latitude + ',' + longitude + '\n'
		if data != '':
			write_handle = open(file, 'w')
			write_handle.write(data)