from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('claim/<int:food_id>/', views.claim_food, name='claim_food'),
]
