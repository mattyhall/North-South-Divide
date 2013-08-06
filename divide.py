from flask import Flask, render_template
from lib.main import *
import json

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/data')
def data():
    data = do_all_of_it_terrible_function_name_im_so_sorry_forgive_me()
    return json.dumps(data)

if __name__ == '__main__':
    # app.debug = True
    # do_all_of_it_terrible_function_name_im_so_sorry_forgive_me()
    app.run(debug=True)
