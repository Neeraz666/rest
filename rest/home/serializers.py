from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):

        if data['age']<18:
            raise serializers.ValidationError({'error': 'Age cant be less than 18.'})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                        raise serializers.ValidationError({'error':'Name cant be numeric.'})

        return data