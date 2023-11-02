from . import api
from flask_restful import Resource

class PedestrianStatsResource(Resource):
    def get(self):
        return {"message": "API is working!"}

api.add_resource(PedestrianStatsResource, '/pedestrian-stats')