from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Department
from .serializers import DepartmentSerializer


@csrf_exempt
def departmentAPI(request, id=0):
    if request.method == 'GET':
        try:
            if id == 0:
                departments = Department.objects.all()
                departments_serializer = DepartmentSerializer(departments, many=True)
            else:
                department = Department.objects.get(dep_id=id)
                departments_serializer = DepartmentSerializer(department)
            return JsonResponse(departments_serializer.data, safe=False)
        except Department.DoesNotExist:
            return JsonResponse({'error': 'Department does not exist.'}, status=404)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully", safe=False, status=201)
        return JsonResponse(department_serializer.errors, status=400)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(dep_id=department_data['dep_id'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully", safe=False, status=201)
        return JsonResponse(department_serializer.errors, status=400)



    elif request.method == 'DELETE':
        try:
            department = Department.objects.get(dep_id=id)
        except Department.DoesNotExist:
            return JsonResponse({'error': 'Department does not exist.'}, status=404)

        department.delete()

        return JsonResponse("Deleted Successfully", safe=False)
