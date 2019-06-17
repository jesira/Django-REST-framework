from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Owner
from .serializers import EmployeeSerializer, OwnerSerializer


class EmployeeList(APIView):

    def get(self, request):
        page = int(request.GET.get('page'))
        emp = Employee.objects.filter(is_deleted=False)
        if page:
            emp = list(emp)[((4*page)-4):4*page]
        # converting all objects to json
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        emp = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        event = get_object_or_404(Employee, id=id)
        event.is_deleted = True
        event.save()
        return Response(str(event.firstname) + ' Deleted!')


class OwnerList(APIView):

    def get(self, request):
        emp = Owner.objects.filter(is_deleted=False)
        # converting all objects to json
        serializer = OwnerSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OwnerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        owner = get_object_or_404(Owner, id=id)
        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        event = get_object_or_404(Owner, id=id)
        event.is_deleted = True
        event.save()
        return Response(str(event.firstname) + ' Deleted!')
