from django.urls import path
from .views import StudentHome,StudentList,StudentForm,StudentDelete
urlpatterns=[
    path('',StudentForm,name='student_form'),
    path('<int:id>/',StudentForm,name='student_edit'),
    path('delete/<int:id>',StudentDelete,name='student_delete'),
    path('list/',StudentList,name='student_list'),
    
]