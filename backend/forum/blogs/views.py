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

## obtener blog por id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBlogById(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


## crear blog
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postBlog(request):
    data = request.data
    blog = Blog.objects.create(
        user = request.user,
        body = data['body'],
    )
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


## actualizar blog
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateBlog(request, pk):
    data = request.data
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data= data)
    # verificar que el usuario logueado es el que actualiza
    if blog.user == request.user:
        if serializer.is_valid():
            serializer.save()
    else:
        return Response({'Error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.data)


## borrar un blog
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if blog.user == request.user:
        blog.delete()
        return Response('blog eliminado')
    else:
        return Response({'Error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)  
    

## crear un comentario
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createComment(request, pk):
    # obtenemos la publicacion en la que queremos comentar
    blog = Blog.objects.get(id=pk)
    user = request.user
    data = request.data
    # creamos el comentario
    comment = Comment.objects.create(
        user = user,
        blog = blog,
        text = data['text']
    )
    comments = blog.comment_set.all()
    blog.save()
    return Response('comment!!')