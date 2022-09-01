from rest_framework import generics
from blog.models import Post
from .serializers import postSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializer
    

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = postSerializer

