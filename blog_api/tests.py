from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTest(APITestcase):

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        def create_post(self):
            self.testuser1 = User.objects.create_user(
                username = 'test_user1', password = '123455678'
            )

            data = {"title": "new", "author": 1, 
                    "excerpt": "new", "content": "new"}