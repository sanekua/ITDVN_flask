import http
import json
from dataclasses import dataclass
from unittest.mock import patch

from src import app


@dataclass
class FakeFilm:
    title = "Fake Film "
    distributed_by = "Fake Film"
    release_date = "2020-10-2"
    length= 10
    rating=5.0


class TestFilms:
    uuid = []

    def test_get_films_with_db(self):
        client = app.test_client()
        resp = client.get('/films')

        assert resp.status_code == http.HTTPStatus.OK

    @patch('src.services.film_service.FilmService.fetch_all_films', autospec=True)
    def test_get_films_mock(self, mock_db_call):
        client = app.test_client()
        resp = client.get('/films')

        mock_db_call.assert_called_once()
        assert resp.status_code == http.HTTPStatus.OK
        assert len(resp.json) == 0

    def test_create_film_with_db(self):
        client = app.test_client()
        data = {
            'title': "Test title1",
            'distributed_by': "Test company",
            'release_date': "2010-10-1",
            'description': "Some test information",
            'length': 150,
            'rating': 8.0,
        }

        resp = client.post('/films', data=json.dumps(data), content_type='application/json')
        print(resp.json)
        assert resp.status_code == http.HTTPStatus.CREATED
        assert resp.json['title'] == "Test title1"
        self.uuid.append(resp.json['uuid'])

    def test_create_film_with_moc(self):
        with patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            client = app.test_client()
            data = {
                'title': "Test title 2",
                'distributed_by': "Test company 2",
                'release_date': "2010-10-2",
                'description': "Some test information about 2 test",
                'length': 100,
                'rating': 6.0,
            }

            resp = client.post('/films', data=json.dumps(data), content_type='application/json')
            print(resp.json)
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()
            assert resp.status_code == http.HTTPStatus.CREATED
            assert resp.json['title'] == "Test title 2"
            self.uuid.append(resp.json['uuid'])

    def test_update_test_with_db(self):
        client = app.test_client()
        url = f'/films/{self.uuid[0]}'
        resp = client.put()
        data = {
            'title': "Test title Updated",
            'distributed_by': "Test company 2",
            'release_date': "2010-10-2",
            'description': "Some test information about 2 test",
            'length': 100,
            'rating': 6.0,
        }

        resp = client.put(url, data=json.dumps(data), content_type='application/json')

        # resp = client.post('/films', data=json.dumps(data), content_type='application/json')
        # print(resp.json)
        # mock_session_add.assert_called_once()
        # mock_session_commit.assert_called_once()
        assert resp.status_code == http.HTTPStatus.OK
        assert resp.json['title'] == "Test title Updated"
        self.uuid.append(resp.json['uuid'])

    def test_update_test_with_mock_db(self):
        with patch('src.services.film_service.FilmService.fetch_film_by_uuid') as mocked_query, \
                patch('src.db.session.add', autospec=True) as mock_session_add, \
                patch('src.db.session.commit', autospec=True) as mock_session_commit:
            mocked_query.return_value= FakeFilm()
            client = app.test_client()
            url = f'/films/90f1a575-b00a-47f1-9d7a-74ecb4116b13'

            a = mocked_query.return_value

            data = {
                'title': a.title,
                'distributed_by': a.distributed_by,
                'release_date': a.release_date,
                'description': 'Desscriptiom',
                'length': a.length,
                'rating': a.rating
            }

            resp = client.put(url, data=json.dumps(data), content_type='application/json')

            # resp = client.post('/films', data=json.dumps(data), content_type='application/json')
            print('reesssssssppppppppppp',resp.json)
            mock_session_add.assert_called_once()
            mock_session_commit.assert_called_once()
            #assert 0
            assert resp.status_code == http.HTTPStatus.OK
            assert resp.json['title'] == "Fake Film "

            #self.uuid.append(resp.json['uuid'])


    def test_delete(self):
        client = app.test_client()
        resp = client.delete(f'films/{self.uuid[0]}')

        assert resp.status_code == http.HTTPStatus.NO_CONTENT

