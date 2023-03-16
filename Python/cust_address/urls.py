from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all_addresses),
    path('<int:pk>/', views.address_detail),
    path('changes/', views.address_create),
]
