
from src import api
from src.resources.agregations import AggregationApi
from src.resources.auth import AuthRegister, AuthLogin

from src.resources.films import FilmListApi
from src.resources.smoke import Smoke
from src.resources.actors import ActorsListApi




# class S1(Resource):
#     def get(self):
#         return {"message": "OK"}, 200


#
# def get_all_films():
#     return [
#         {
#             'id': '1',
#             'title': 'Avatar',
#             'release_date': "November 4, 2020",
#         },
#         {
#             'id': '2',
#             'title': 'Forsage 2',
#             'release_date': "January 11, 2010",
#         },
#         {
#             'id': '3',
#             'title': 'Harry Potter 1 part',
#             'release_date': "November 14, 2011",
#         },
#         {
#             'id': '4',
#             'title': 'Harry Potter 2 part',
#             'release_date': "January 1, 2009",
#         },
#         {
#             'id': '5',
#             'title': 'Awesome',
#             'release_date': "August 22, 2006",
#         },
#         {
#             'id': '6',
#             'title': 'Hacker',
#             'release_date': "September 1, 2006",
#         },
#     ]


# def get_film_by_uuid(uuid: str) -> dict:
#     films = get_all_films()
#     print('iiiii',uuid)
#     print(films[0]['id'] == uuid)
#     film = list(filter(lambda f: f['id'] == uuid, films))
#     print(film)
#     return film[0] if film else {}
#
#
# def create_film(film_json: dict) -> List[dict]:
#     films = get_all_films()
#     films.append(film_json
#                  )
#     return films



api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
api.add_resource(ActorsListApi, '/actors', '/actors/<uuid>', strict_slashes=False)
api.add_resource(AggregationApi, '/aggregations', strict_slashes=False)
api.add_resource(AuthRegister, '/register', strict_slashes=False)
api.add_resource(AuthLogin, '/login', strict_slashes=False)

