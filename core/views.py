from django.shortcuts import render, redirect
from .models import FoodPost
from django.utils import timezone
from django.contrib import messages
def home(request):
    food_posts = FoodPost.objects.filter(
        expiry_time__gt=timezone.now(),
        is_claimed=False
    )
    return render(request, 'core/home.html', {'food_posts': food_posts})

def claim_food(request, food_id):
    food = FoodPost.objects.get(id=food_id)
    food.is_claimed = True
    food.save()
    messages.success(request, "Food claimed successfully!")
    return redirect('home')
