from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
# Create your views here.
from .models import *
from .Ser import *

# Create your views here.

@api_view(['get'])
@permission_classes([AllowAny])
def apiGetProducts(request):

    allDatas = Product.objects.all().order_by('-id')
    DATA = ProductSer(allDatas, many=True).data

    return Response(DATA)

@api_view(['get'])
@permission_classes([AllowAny])
def apiGetTypes(request):

    allDatas = Type.objects.all().order_by('-id')
    DATA = TypeSer(allDatas, many=True).data

    return Response(DATA)
