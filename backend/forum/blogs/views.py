from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status

from .serializers import BlogSerializer
from .models import Blog, Comment
from users.models import User

## obtener los blogs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBlogs(request):
    ## ordena los blogs desde el ultimo hasta el primero
    blog = Blog.objects.filter().order_by('-date')
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)