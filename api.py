from flask import Flask, jsonify
#from flask_restful import Resource, Api
from random import randint

app = Flask(__name__)
#api = Api(app)


facts = [
    {
        'id': 1,
        'fact' : "Luchadors wrestle because they wish to be hugged"
    },
    {
        'id': 2,
        'fact': "Luchadors wear masks because they are too handsome"
    }
]

@app.route('/facts', methods=['GET'])
def get_facts():
    return jsonify({'facts': facts})


@app.route('/facts/<int:fact_id>', methods=['GET'])
def get_fact(fact_id):
    fact = [fact for fact in facts if fact['id'] == fact_id]
    if len(fact) == 0:
        abort(404)
    return jsonify({'fact': fact[0]})

@app.route('/facts/random', methods=['GET'])
def get_random():
    fact_id = randint(1, len(facts))
    fact = [fact for fact in facts if fact['id'] == fact_id]
    return jsonify({'fact': fact[0]})


if __name__ == '__main__':
    app.run(debug = True)