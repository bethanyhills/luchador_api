from app import db


# Create our database model
class Fact(db.Model):
    __tablename__ = 'facts'
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String, unique=True)

    def __init__(self, fact):
        self.fact = fact

    def __repr__(self):
        return '<Fact %r>' % self.fact

    def create_fact(data):
        x = Fact(fact=data)
        db.session.add(x)
        db.session.commit()
        return jsonify({'id': x.id, 'fact': x.fact}), 201
    
    def serialize(self):
        return {
            'id': self.id,
            'fact': self.fact,
            'uri': url_for('get_fact', fact_id=self.id, _external=True)
        }

# Create our user model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, username):
        self.username = username
        self.password = str(uuid.uuid4())

    def __repr__(self):
        return '<Name: {}, Password: {}, ID: {}>'.format(self.username, self.password, self.id)