from django.urls import path

from .import views

urlpatterns=[
    path('list/', views.Companylist.as_view(), name='list'),
    path('detail/<int:pk>/',views.CompanyDetailView.as_view(), name='detail'),
    path('create/',views.CreateCompanyView.as_view(), name='create'),
    path('update/<int:pk>/',views.UpdateCompanyView.as_view(),name='update'),
    path('delete/<int:pk>/',views.DeleteCompanyView.as_view(),name='delete'),
    path('Jlist/',views.Jobslist.as_view(), name='jlist'),
    path('Cjobs/',views.CreateJobsView.as_view(), name='Jcreate'),
    path('Jdetail/<int:pk>',views.JobsDetailView.as_view(), name='jdetail'),
    path('jupdate/<int:pk>',views.JobsUpdateView.as_view(), name='jupdate'),
    path('Jdelete/<int:pk>',views.JobsDeleteView.as_view(), name='deleteJ'),
]