from rest_framework import serializers
from .models import *

class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class TypeSer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name', 'img']