from rest_framework import serializers
from . models import Department, Office, Employee
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('dep_id', 'dep_code', 'dep_name', 'dep_description', 'created_at', 'updated_at')

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('off_id', 'off_code', 'off_name', 'off_description', 'dep_code', 'created_at', 'updated_at')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id', 'emp_code', 'emp_name', 'emp_birthdate', 'emp_gender', 'emp_nationality',
                  'emp_marital_status', 'emp_age', 'emp_address', 'emp_email', 'emp_phone',
                  'off_code', 'dep_code', 'created_at', 'updated_at')
