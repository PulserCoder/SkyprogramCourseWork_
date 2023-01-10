from flask import Blueprint, jsonify
from app.dao.search_posts_dao import SearchPostsDAO
import logging
from config import Config

"""Settings of logger"""
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler = logging.FileHandler(Config.PATH_TO_LOG)
file_handler.setFormatter(formatter)
main_logger = logging.getLogger('main')
main_logger.addHandler(file_handler)
main_logger.setLevel(logging.DEBUG)

"""Instance of DAO"""
search_dao = SearchPostsDAO()
posts_api_blueprint = Blueprint("api_get_info_posts", __name__)


@posts_api_blueprint.route('/api/posts')
def get_info_all_posts():
    """Return to user all info from json about posts"""
    main_logger.info('Запрос на получения полного списка постов')
    return jsonify(search_dao.get_posts_all())


@posts_api_blueprint.route('/api/posts/<int:pk>')
def get_info_one_post(pk):
    """Return to user info from json about 1 posts which user put in link"""
    main_logger.info(f'Запрос на получение одного поста {pk}')
    return jsonify(search_dao.get_post_by_pk(pk))