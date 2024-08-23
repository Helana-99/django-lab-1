from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainee_list, name='trainee_list'),
    path('create/', views.trainee_create, name='trainee_create'),
    path('<int:id>/update/', views.trainee_update, name='trainee_update'),
    path('<int:id>/delete/', views.trainee_delete, name='trainee_delete'),
    path('<int:id>/details/', views.trainee_details, name='trainee_details'),
]
