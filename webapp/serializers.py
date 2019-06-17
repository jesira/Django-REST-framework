from rest_framework import serializers
from . models import Employee,Owner


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
#       fields = ('firstname', 'lastname')
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
#       fields = ('firstname', 'lastname')
        fields = '__all__'
