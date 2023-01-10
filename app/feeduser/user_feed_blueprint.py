from flask import Blueprint, render_template
from exeptions import PathIsNotCorrect
from app.dao.search_posts_dao import SearchPostsDAO

user_feed_blueprint = Blueprint('user_feed', __name__, template_folder='templates')
search_dao = SearchPostsDAO()


@user_feed_blueprint.route('/users/<username>', methods=['GET'])
def show_user_profile(username):
    """Return one user page by username with his posts"""
    try:
        return render_template('user-feed.html', username=username, posts=search_dao.get_posts_by_user(username))
    except (PathIsNotCorrect, ValueError):
        return 'Not founded'
