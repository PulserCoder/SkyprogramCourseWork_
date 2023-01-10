from flask import Blueprint, render_template, request
from app.dao import search_posts_dao
from exeptions import PathIsNotCorrect

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

search_posts_dao = search_posts_dao.SearchPostsDAO()


@main_blueprint.route('/', methods=['GET'])
def start_page_index():
    """Return to user main index page"""
    try:
        return render_template('index.html', posts=search_posts_dao.get_posts_all())
    except (ValueError, PathIsNotCorrect):
        return 'В данный момент времени сервер не доступен и работает неисправлно. Наши разработчики уже знают об этой проблеме.'


@main_blueprint.route('/search/', methods=['GET'])
def search_posts():
    """Return to user posts with part of content"""
    try:
        search_request = request.args.get('s')
        correct_posts = search_posts_dao.search_for_posts(search_request)
        quantity_of_posts = len(correct_posts)
        return render_template('search.html', quantity=quantity_of_posts, posts=correct_posts)
    except (ValueError, PathIsNotCorrect):
        return 'Такого поста нет <a href="/"> Назад</a>'