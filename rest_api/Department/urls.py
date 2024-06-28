from django.urls import path, include
from . import views

urlpatterns = [
    path('department', views.departmentAPI),
    path('department/<int:id>', views.departmentAPI), #to accepting ID as integer call or request

    ]