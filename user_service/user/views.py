from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
# Create your views here.

#function to get all user's data and perform the operation on it
@api_view(['GET', 'DELETE', 'PUT'])
def user_detail(request, user_id):
    try:
        user_obj = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = UserSerializer(user_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        user_obj.delete()
        return Response(status=204)
    else:
        return Response(status=400)

#function to get all user's data
#function for the creation of new user
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        user_obj = User.objects.all()
        serializer = UserSerializer(user_obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(str(serializer.data['user_id']))
            requests.post('http://127.0.0.1:8001/api/content/update',{'user_id':str(serializer.data['user_id'])})
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:
        return Response(status=400)

#function to get all existing user's data
@api_view(['post'])
def user_update(request):
    if request.method == 'POST':
        data=request.data
        user=User.objects.all().values('user_id').count()
        data["user_id"]=user
        print(data)
        url='http://127.0.0.1:8002/api/daily_pass/update_user/'
        r=requests.post(url,data)
        return Response(status=202)
    return Response(status=400)