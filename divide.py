from flask import Flask, render_template, request
from lib.work import work
from lib.loaders.policedata import PoliceData
from lib.loaders.populationdata import PopulationData
import json

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html', data_set=int(request.args.get('dataset', 0)), 
                                         no_line=request.args.get('noline', False),
                                         heat_map=request.args.get('heatmap', False))

@app.route('/data')
def data():
    data_set = int(request.args.get('dataset', 0))
    if data_set == 0:
        data_set = PoliceData()  
    elif data_set == 1:
        data_set = PopulationData()
    data_set.load() 
    data = work(data_set)   
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
