from flask_restful import Resource

class ProfileResource(Resource):
    def get(self):
        return {'hello': 'world'}