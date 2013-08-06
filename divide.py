from flask import Flask, render_template
from lib.main import *
import json

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/data')
def data():
	data_set = request.args.get('data', 0)
	if data_set == 0:
	    directory = './data/street_crime/'
	    data_set = PoliceData()
	    data_set.load(directory)	
	    data = work(data_set)
	    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)
