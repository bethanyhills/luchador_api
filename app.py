import os
from flask import (Flask, 
                    jsonify, 
                    abort, 
                    make_response,
                    request
                    )
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.heroku import Heroku
from random import randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# heroku = Heroku(app)
db = SQLAlchemy(app)


# Create our database model
class Fact(db.Model):
    __tablename__ = 'facts'
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(120), unique=True)

    def __init__(self, fact):
        self.fact = fact

    def __repr__(self):
        return '<Fact %r>' % self.fact

    def serialize(self):
        return {
            'id': self.id,
            'fact': self.fact
        }



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#GET
@app.route('/facts', methods=['GET'])
def get_facts():
    all_facts = Fact.query.all()
    if len(all_facts) > 0:
        return jsonify(facts=[x.serialize() for x in all_facts])


@app.route('/facts/<int:fact_id>', methods=['GET'])
def get_fact(fact_id):
    x = Fact.query.get(fact_id)
    if not x:
        abort(404)
    return jsonify({'id': x.id, 'fact': x.fact})

@app.route('/facts/random', methods=['GET'])
def get_random():
    all_facts = Fact.query.all()
    fact_id = randint(1, len(all_facts))
    x = Fact.query.get(fact_id)
    if not x:
        abort(404)
    return jsonify({'id': x.id, 'fact': x.fact})

#POST
@app.route('/facts', methods=['POST'])
def create_fact():
    if not request.json or not 'fact' in request.json:
        abort(400)

    post_request = Fact.query.filter_by(fact=request.json.get('fact')).first()
    if not post_request:
        x = Fact(fact=request.json.get('fact'))
        db.session.add(x)
        db.session.commit()
        return jsonify({'id': x.id, 'fact': x.fact}), 201
    else:
        return make_response(jsonify({'error': 'That fact already exists'}), 404)

#PUT
@app.route('/facts/<int:fact_id>', methods=['PUT'])
def update_fact(fact_id):
    if len(request.json.get('fact')) == 0:
        abort(404)
    if not request.json:
        abort(400)
    #if the fact exists, update it
    x = Fact.query.get(fact_id)
    if x:
        x.fact = request.json.get('fact')
        db.session.add(x)
        db.session.commit()
        return jsonify({'id': x.id, 'fact': x.fact})
    #else create the fact
    else:
        return make_response(jsonify({'error': 'That fact doesnt exist'}), 404)


if __name__ == '__main__':
    app.run(debug = True)

