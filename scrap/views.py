from django.shortcuts import render
from .models import Vehicle
from rest_framework.response import Response
from rest_framework.views import APIView
from .serialzers import vehicleSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

def user(request):
    data = {
        'first_user':Vehicle.objects.get(id=4)
    }
    return render(request,'User.html',data)

class List(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        vehicles = Vehicle.objects.all()
        result = paginator.paginate_queryset(vehicles,request)
        serializer = vehicleSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)
    
class Api(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = vehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
