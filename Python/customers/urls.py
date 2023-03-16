from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all_customers),
    path('<int:pk>/', views.customer_detail),
    path('changes/', views.customer_create),
]
