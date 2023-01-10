from flask import Flask
from app.main.main_blueprint import main_blueprint
from app.posts.post_blueprint import post_blueprint
from app.feeduser.user_feed_blueprint import user_feed_blueprint
from app.api.posts_api_blueprint import posts_api_blueprint


"""Setting of Flask application"""
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(posts_api_blueprint)


@app.errorhandler(404)
def not_found_error(error):
    return f'<h1>{error}</h1>'


@app.errorhandler(500)
def error_on_server(error):
    return f'<h1>{error}</h1>'


if __name__ == '__main__':
    app.run()
