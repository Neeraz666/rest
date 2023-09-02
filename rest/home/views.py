from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def get_book(request):
     bookobjs = Book.objects.all()
     serializer = BookSerializer(bookobjs, many = True)
     return Response({'status':200, 'Books':serializer.data})


class RegisterUser(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})

        serializer.save()
        
        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'payload': serializer.data,'token': str(token_obj) ,'message': 'Your data is saved.'})



class StudentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        studentobj = Student.objects.all()
        serializer = StudentSerializer(studentobj, many=True)
        return Response({'status':200, 'message':serializer.data})

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})

        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'Your data is saved.'})

    def put(self, request):
        pass

    def patch(self, request):
        try:
            studentobj = Student.objects.get(id=request.data['id'])

            serializer = StudentSerializer(studentobj, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})

            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'Your data is saved.'})
    
        except Student.DoesNotExist:
            return Response({'status': 403, 'message': 'Invalid id.'})
        
    def delete(self, request):
        try:
            id = request.GET.get('id')
            studentobj = Student.objects.get(id=id)
            studentobj.delete()
            return Response({'status':200, 'message':'deleted'})
    
        except Exception as e:
             print(e)
             return Response({'status':403, 'message':'invalid id '})   
