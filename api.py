from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


facts = {
    '1': "Luchadors wrestle because they wish to be hugged",
    '2': "Luchadors wear masks because they are too handsome"}

class LuchadorFacts(Resource):
    def get(self, fact_id):
            return {fact_id: facts[fact_id]}



# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

api.add_resource(LuchadorFacts, '/<string:fact_id>')

if __name__ == '__main__':
    app.run(debug = True)