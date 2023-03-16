from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all_orders),
    path('<int:pk>/', views.order_detail),
    path('changes/', views.order_create),
]
