from django.test import TestCase
from .models import Post
# Create your tests here.


class PostModelTest(TestCase):
  def test_post_model_exists(self):
    posts = Post.objects.count()
    self.assertEqual(posts, 0)
    
  def test_string_representation(self):
    post = Post(title="title")
    self.assertEqual(str(post), post.title)