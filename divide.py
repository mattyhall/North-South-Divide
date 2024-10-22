from flask import Flask, render_template, request
from lib.work import work
from lib.loaders.policedata import PoliceData
from lib.loaders.populationdata import PopulationData
from lib.loaders.childpovertydata import ChildPovertyData
from lib.loaders.cancerdata import CancerData
import json

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html', police=request.args.get('police', 'false'),
                                         population=request.args.get('population', 'false'), 
                                         child_poverty=request.args.get('childpoverty', 'false'),
                                         cancer=request.args.get('cancer', 'false'),
                                         no_line=request.args.get('noline', 'false'),
                                         heat_map=request.args.get('heatmap', 'false'),
                                         step=float(request.args.get('step', '0.2')),
                                         realistic=request.args.get('realistic', 'false'))

@app.route('/data')
def data():
    police = request.args.get('police', 'true')
    population = request.args.get('population', 'false')
    child_poverty = request.args.get('childpoverty', 'false')
    cancer = request.args.get('cancer', 'false')
    step = float(request.args.get('step', '0.2'))
    data_sets = []
    if police == 'true':
        data_set = PoliceData()  
        data_set.load()
        data_sets.append(data_set)
    if population == 'true':
        data_set = PopulationData()
        data_set.load()
        data_sets.append(data_set)
    if child_poverty == 'true':
        data_set = ChildPovertyData()
        data_set.load()
        data_sets.append(data_set)
    if cancer == 'true':
        data_set = CancerData()
        data_set.load()
        data_sets.append(data_set)
    output = {}
    average = 0
    for data_set in data_sets:
        data = work(step, data_set)
        output[data_set.NAME] = data
        average += data['average_line'][0]['latitude']
    average /= len(data_sets)
    output['average'] = [{'latitude': average, 'longitude': -5}, {'latitude': average, 'longitude': 2}]
    return json.dumps(output)

if __name__ == '__main__':
    app.run(debug=True)
