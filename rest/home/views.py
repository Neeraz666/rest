from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def home(request):
    studentobj = Student.objects.all()
    serializer = StudentSerializer(studentobj, many=True)
    return Response({'status':200, 'message':serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})

    serializer.save()
    return Response({'status': 200, 'payload': serializer.data, 'message': 'Your data is saved.'})

@api_view(['PUT', 'PATCH'])
def update_student(request, id):
    try:
        studentobj = Student.objects.get(id=id)

        serializer = StudentSerializer(studentobj, data=request.data, partial=True)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})

        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'Your data is saved.'})
    
    except Student.DoesNotExist:
        return Response({'status': 403, 'message': 'Invalid id.'})

@api_view(['DELETE'])
def delete_student(request, id):
        try:
             studentobj = Student.objects.get(id=id)
             studentobj.delete()
             return Response({'status':200, 'message':'deleted'})
        
        except Exception as e:
             print(e)
             return Response({'status':403, 'message':'invalid id '})   