from flask import Flask

app = Flask(__name__)

race_dictionary = {'10k': 10000.0, '5k': 5000.0, 'half-marathon' : 21300}

@app.route('/race_types')
def race_types():
    return {'race_types' : list(race_dictionary.values())}

@app.route('/race_distance/<race_string>')
def race_distance(race_string):
    return {'distance': race_dictionary[race_string]}