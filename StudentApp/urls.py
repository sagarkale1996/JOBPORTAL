from .import views
from django.urls import path
urlpatterns = [
    path('Sadd/',views.Add_student, name = 'ADDSTU'),
    path('Sview/',views.View_stu, name = 'SView'),
    path('Sdelete/<int:id>/', views.Delete_student, name = 'SDelete'),
    path('Supdate/<int:id>/',views.Update_Student, name = 'Supdate')
]