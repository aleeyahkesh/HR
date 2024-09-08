from django.urls import path
from emp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.allemployees, name='allemployees'),
    path('allemployees/', views.allemployees, name= 'allemployees'),
    path('employeedetails/<int:id>', views.employeedetails, name='employeedetails'),
    path('employeedelete/<int:id>', views.employeedelete, name='employeedelete'),
    path('employeeupdate/<int:id>', views.employeeUpdate, name='employeeupdate'),
    path('addemployee', views.addemployee, name='addemployee'),
    path('doupdateemployee/<int:id>/', views.doupdateemployee, name= 'doupdateemployeee'),
    #path('employeeparttime', views.BulkInsert, name='employeeparttime'),
    #path('',emp.views.myview, name='emp_myview')
]


