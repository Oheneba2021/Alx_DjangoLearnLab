from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .models import Post

User = get_user_model()


class PostCommentTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="u1", password="pass12345")
        self.user2 = User.objects.create_user(username="u2", password="pass12345")
        self.token1 = Token.objects.create(user=self.user1)
        self.token2 = Token.objects.create(user=self.user2)

    def auth(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

    def test_user_can_create_post(self):
        self.auth(self.token1.key)
        res = self.client.post("/api/posts/", {"title": "T", "content": "C"}, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().author, self.user1)

    def test_user_cannot_edit_others_post(self):
        post = Post.objects.create(author=self.user1, title="T", content="C")
        self.auth(self.token2.key)
        res = self.client.patch(f"/api/posts/{post.id}/", {"content": "hacked"}, format="json")
        self.assertEqual(res.status_code, 403)