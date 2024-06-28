from django.db import models

class Department(models.Model):
    dep_id = models.AutoField(primary_key=True)
    dep_code = models.CharField(max_length=100)
    dep_name = models.CharField(max_length=100)
    dep_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Office(models.Model):
    off_id = models.AutoField(primary_key=True)
    off_code = models.CharField(max_length=100)
    off_name = models.CharField(max_length=100)
    off_description = models.CharField(max_length=100)
    dep_code = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_code = models.CharField(max_length=100)
    emp_name = models.CharField(max_length=100)
    emp_birthdate = models.DateField()
    emp_gender = models.CharField(max_length=100)
    emp_nationality = models.CharField(max_length=100)
    emp_marital_status = models.CharField(max_length=100)
    emp_age = models.CharField(max_length=100)
    emp_address = models.CharField(max_length=100)
    emp_email = models.CharField(max_length=100)
    emp_phone = models.CharField(max_length=100)
    off_code = models.ForeignKey(Office, on_delete=models.CASCADE)
    dep_code = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


