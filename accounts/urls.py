from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('doctors/', views.DoctorList.as_view()),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view()),
    # path('doctors/<int:pk>/delete/', views.DoctorDelete.as_view()),
    # path('doctors/<int:pk>/create/', views.DoctorCreate.as_view()),
]