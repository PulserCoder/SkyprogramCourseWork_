import pytest
from app.dao.search_posts_dao import SearchPostsDAO, Post


@pytest.fixture()
def dao_example():
    return SearchPostsDAO()


keys_should_be = {'poster_name', 'pk', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count'}
keys_should_be_for_comments = {'post_id', 'commenter_name', 'comment', 'pk'}

class TestSearchPostsDAO:
    def test_load_posts(self, dao_example):
        assert len(dao_example.load_posts()) > 0, 'Не подгружается json'
        assert type(dao_example.load_posts()) == list, 'Неправильный формат файла'
        assert set(dao_example.load_posts()[0].keys()) == keys_should_be

    def test_load_comments(self, dao_example):
        assert len(dao_example._load_comments()) > 0, 'Не подгружается json'
        assert type(dao_example._load_comments()) == list, 'Неправильный формат файла'
        assert set(dao_example._load_comments()[0].keys()) == keys_should_be_for_comments

    def test_convert_post(self, dao_example):
        assert type(dao_example._convert_post(dao_example.get_post_by_pk(1))) == dict
        assert dao_example._convert_post(dao_example.get_post_by_pk(1))['pk'] == 1

    def test_valid_posts_and_comments(self, dao_example):
        assert dao_example._valid_posts_and_comments(dao_example.get_posts_all()) > 0, 'пустой список дядя'
        with pytest.raises(ValueError):
            dao_example._valid_posts_and_comments([])

    def test_get_posts_all(self, dao_example):
        assert type(dao_example.get_posts_all()) == list
        assert type(dao_example.get_posts_all()[0]) == dict
        assert dao_example.get_posts_all()[0]['pk'] == 1

    def test_get_post_by_users(self, dao_example):
        assert type(dao_example.get_posts_by_user('leo')) == list
        assert type(dao_example.get_posts_by_user('leo')[0]) == dict
        assert dao_example.get_posts_by_user('leo')[0]['poster_name'] == 'leo'

    def test_get_comments_by_post_id(self, dao_example):
        assert type(dao_example.get_comments_by_post_id(1)) == list
        assert type(dao_example.get_comments_by_post_id(1)[0]) == dict
        assert dao_example.get_comments_by_post_id(1)[0]['commenter_name'] == 'hanna'

    def test_search_posts(self, dao_example):
        assert type(dao_example.search_for_posts('еда')) == list
        assert len(dao_example.search_for_posts('еда')) == 1
        assert dao_example.search_for_posts('еда')[0]['content'] == dao_example.get_posts_all()[0]['content']

    def test_get_post_by_pk(self, dao_example):
        assert type(dao_example.get_post_by_pk(1)) == dict
        assert dao_example.get_post_by_pk(1)['pk'] == dao_example.get_posts_all()[0]['pk']