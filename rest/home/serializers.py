from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):

        if 'age' in data and data['age']<18:
            raise serializers.ValidationError({'error': 'Age cant be less than 18.'})
        
        if 'name' in data and data['name']:
            for n in data['name']:
                if n.isdigit():
                        raise serializers.ValidationError({'error':'Name cant be numeric.'})

        return data
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'