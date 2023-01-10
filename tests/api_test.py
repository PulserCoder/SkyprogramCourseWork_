import pytest
from run import app


class TestAPI:
    def test_get_info_all_posts(self):
        assert app.test_client().get('/api/posts').status_code == 200
        assert type(app.test_client().get('/api/posts').json) == list
        assert set(app.test_client().get('/api/posts').json[0].keys()) == {'content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count'}

    def test_info_one_post(self):
        assert type(app.test_client().get('/api/posts/1').json) == dict
        assert set(app.test_client().get('/api/posts/1').json.keys()) == {'content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count'}