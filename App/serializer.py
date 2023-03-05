from .models import Employee
from rest_framework import serializers
 
class Empserializer(serializers.Serializer):
    Name=serializers.CharField
    Email=serializers.EmailField
    mobile=serializers.IntegerField
    department=serializers.CharField
    collage=serializers.CharField
    salary=serializers.IntegerField

