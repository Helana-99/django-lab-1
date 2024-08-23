from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_list, name='account_list'),
    path('create/', views.account_create, name='account_create'),
    path('<int:id>/update/', views.account_update, name='account_update'),
    path('<int:id>/delete/', views.account_delete, name='account_delete'),
    path('<int:id>/', views.account_details, name='account_details'),
]
