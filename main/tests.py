from django.test import TestCase
from django.test import TestCase
from .models import Profile,Project, Rating
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.username = User(id=1, username='cindy', password='hyte4vvd4')
        self.username.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.username, User))

    def test_save_user(self):
        self.username.save()

    def test_delete_user(self):
        self.username.delete()


class TestPost(TestCase):
    def setUp(self):
        self.username = User.objects.create(id=1, username='cindy')
        self.post = Project.objects.create(id=1, title='test post', image='great.jpeg',
                                        description='desc', username=self.username, link='http://url.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Project.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Project.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Project.search_post('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Project.search_post('test')
        self.assertTrue(len(post) < 1)


