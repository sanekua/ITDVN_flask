from datetime import datetime

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm import selectinload

from src import db
from src.database.models2 import Film
from src.resources.auth import token_required
from src.schemas.films import FilmSchema
from src.services.film_service import FilmService


class FilmListApi(Resource):
    film_schema = FilmSchema()

    # @token_required
    def get(self, uuid=None):
        print("get method execute")
        if not uuid:
            films = (
                FilmService.fetch_all_films(db.session)
                .options(selectinload(Film.children))
                .all()
            )
            return self.film_schema.dump(films, many=True), 200
        film = FilmService.fetch_film_by_uuid(db.session, uuid=uuid)
        print(type(uuid))
        if not film:
            return "Empty", 404
        return self.film_schema.dump(film), 200

    def post(self):
        # film_json = request.json
        # if not film_json:
        #     return {"message": "Wrong data"}, 404
        # try:
        #     film = Film(
        #         title=film_json['title'],
        #         release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
        #         distributed_by=film_json['distributed_by'],
        #         description=film_json.get('description'),
        #         length=film_json.get('length'),
        #         rating=film_json.get('rating')
        #
        #     )
        #     print(film)
        #     db.session.add(film)
        #     db.session.commit()
        # except (ValueError, KeyError):
        #     return {"message": "Wrong data post exception"}, 400
        # return {"Message": "Created successfully"}, 201
        try:
            film = self.film_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 201

    def put(self, uuid):
        # film_json = request.json
        # if not film_json:
        #     return {"message": "Wrong data"}, 400
        # try:
        #     db.session.query(Film).filter_by(uuid=uuid).update(
        #         dict(
        #             title=film_json['title'],
        #             release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),
        #             distributed_by=film_json['distributed_by'],
        #             description=film_json.get('description'),
        #             length=film_json.get('length'),
        #             rating=film_json.get('rating')
        #         )
        #     )
        #     db.session.commit()
        # except(ValueError, KeyError):
        #     return {"message": "Wrong data exception"}, 400
        #
        # return {"message": "Updated successfully"}, 200
        film = FilmService.fetch_film_by_uuid(db.session, uuid=uuid)
        if not film:
            return {"message": "Wrong data"}, 400
        try:
            film = self.film_schema.load(
                request.json, instance=film, session=db.session
            )
        except ValidationError as e:
            return {"message": str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    def patch(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()

        if not film:
            return {"message": "Wrong data, not film in patch"}, 404

        film_json = request.json
        title = film_json.get("title")
        release_date = (
            datetime.strptime(film_json.get("release_date"), "%B %d %Y")
            if film_json.get("release_date")
            else None
        )
        distributed_by = film_json.get("distributed_by")
        description = film_json.get("description")
        length = film_json.get("length")
        rating = film_json.get("rating")

        if title:
            film.title = title
        elif release_date:
            film.release_date = release_date
        elif distributed_by:
            film.distributed_by = distributed_by
        elif description:
            film.description = description
        elif length:
            film.length = length
        elif rating:
            film.rating = rating

        db.session.add(film)
        db.session.commit()

        return {"message": "Updated successfully"}, 200

    def delete(self, uuid):
        film = FilmService.fetch_film_by_uuid(db.session, uuid=uuid)

        if not film:
            return {"message": "Wrong data, not film in patch"}, 404

        db.session.delete(film)
        db.session.commit()

        return " ", 204
