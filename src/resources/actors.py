from flask_restful import Resource

from src.schemas.actors import ActorSchema


class ActorsListApi(Resource):
    actor_scheme = ActorSchema()

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
