from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('claim/<int:food_id>/', views.claim_food, name='claim_food'),  # claim action
]
