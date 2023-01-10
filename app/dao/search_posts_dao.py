import json
from config import Config
from exeptions import PathIsNotCorrect
from typing import TypedDict

ID_POST = int


class Post(TypedDict):
    poster_name: str
    poster_avatar: str
    pic: str
    content: str
    views_count: int
    likes_count: int
    pk: int


class SearchPostsDAO:
    def load_posts(self) -> list[dict]:
        """load all posts from json"""
        try:
            return json.load(open(Config.PATH, 'r'))
        except FileNotFoundError:
            raise PathIsNotCorrect

    def _load_comments(self):
        """load comments from json"""
        try:
            return json.load(open(Config.PATH_COMMENTS, 'r'))
        except FileNotFoundError:
            raise PathIsNotCorrect

    def _convert_post(self, post: dict) -> Post:
        """Convert post to named dictionary"""
        return Post(poster_name=post['poster_name'],
                    poster_avatar=post['poster_avatar'],
                    pic=post['pic'],
                    content=post['content'],
                    views_count=post['views_count'],
                    likes_count=post['likes_count'],
                    pk=post['pk'])

    def _valid_posts_and_comments(self, data: list[Post]) -> bool:
        if len(data) == 0:
            raise ValueError
        return True

    def get_posts_all(self) -> list[Post]:
        """Return list from posts.json"""
        return [self._convert_post(post) for post in self.load_posts()]

    def get_posts_by_user(self, user_name: str) -> list[Post]:
        """Return list with posts by user"""
        user_post_list = []
        for post in self.get_posts_all():
            if user_name == post['poster_name']:
                user_post_list.append(post)
        self._valid_posts_and_comments(user_post_list)
        return user_post_list

    def get_comments_by_post_id(self, post_id: ID_POST) -> list[dict]:
        """Return list with comments by ID"""
        user_post_list = []
        for comment in self._load_comments():
            if post_id == comment['post_id']:
                user_post_list.append(comment)
        self._valid_posts_and_comments(user_post_list)
        return user_post_list

    def search_for_posts(self, query: str) -> list[Post]:
        """Return list with posts by word"""
        user_post_list = []
        for post in self.get_posts_all():
            if query in post['content']:
                user_post_list.append(post)
        self._valid_posts_and_comments(user_post_list)
        return user_post_list

    def get_post_by_pk(self, pk: ID_POST) -> Post:
        """Return post by pk"""
        for post in self.get_posts_all():
            if pk == post['pk']:
                return post


if __name__ == '__main__':
    print(SearchPostsDAO().get_posts_by_user('leo'))
