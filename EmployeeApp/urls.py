from .import views
from django.urls import path
urlpatterns=[
    path('base/',views.Home, name = 'base'),
    path('Ab/', views.About, name= 'about'),
    path('add/',views.Add_Emp,name='ADDEMP'),
    path('view/',views.View_Emp,name='display'),
    path('edelete/<int:id>/',views.delete, name='Edelete'),
    path('eupdate/<int:id>/',views.Update_Emp, name='EUpdate'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]
