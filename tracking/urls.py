from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracking_list, name='tracking_list'),
    path('create/', views.tracking_create, name='tracking_create'),
    path('<int:id>/update/', views.tracking_update, name='tracking_update'),
    path('<int:id>/delete/', views.tracking_delete, name='tracking_delete'),
    path('<int:id>/details/', views.tracking_details, name='tracking_details'),
]
