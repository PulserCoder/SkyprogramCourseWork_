from flask import Blueprint, render_template
from app.dao.search_posts_dao import SearchPostsDAO
from exeptions import PathIsNotCorrect

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')
search_dao = SearchPostsDAO()


@post_blueprint.route('/posts/<int:post_id>', methods=['GET'])
def show_one_post(post_id):
    """Return page with one post and post's comments"""
    try:
        post_ = search_dao.get_post_by_pk(post_id)
        comments_ = search_dao.get_comments_by_post_id(post_id)
        count_of_comments = len(comments_)
        return render_template('post.html', post=post_, comments=comments_, count_of_comments=count_of_comments)
    except (ValueError, PathIsNotCorrect):
        return 'Error'