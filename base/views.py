from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Item, Todo

from .serializers import TodoSerializer
    

class TodoListApiView(APIView):
    #add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    
#1. List all

def get(self, request, *args, **kwargs):
    '''
    List all the todo items for given requested user
    '''
    todo=Todo.objects.filter(user=request.user.id)
    serializer=TodoSerializer(todo, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

#2. Create

def post(self, request, *args, **kwargs):
    '''
    Cerate the todo with given todo data
    '''
    
    data = {
        'task': request.data.get('task'),
        'completed': request.data.get('completed'),
        }
    
    serializer=TodoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)