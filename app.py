from flask import (Flask, 
                    jsonify, 
                    abort, 
                    make_response,
                    request
                    )
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

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#GET
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

#POST
@app.route('/facts', methods=['POST'])
def create_fact():
    if not request.json or not 'fact' in request.json:
        abort(400)
    fact = {
        'id': len(facts) + 1,
        'fact': request.json.get('fact', '')
    }
    facts.append(fact)
    return jsonify({'fact': fact}), 201

#PUT
# @app.route('/facts/<int:fact_id>', methods=['PUT'])
# def update_fact(fact_id):
#     fact = [fact for fact in facts if fact['id'] == fact_id]
#     if len(fact) == 0:
#         abort(404)
#     if not request.json:
#         abort(400)
#     if 'fact' in request.json and type(request.json['fact']) is not unicode:
#         abort(400)
    
#     fact[0]['fact'] = request.json.get('fact', fact[0]['fact'])
#     return jsonify({'task': task[0]})


if __name__ == '__main__':
    app.run(debug = True)

