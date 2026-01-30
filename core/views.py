from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import FoodPost


def home(request):
    food_posts = FoodPost.objects.filter(
        expiry_time__gt=timezone.now(),
        is_claimed=False
    )
    return render(request, 'core/home.html', {'food_posts': food_posts})


def claim_food(request, food_id):
    if request.method == "POST":
        food = get_object_or_404(FoodPost, id=food_id)

        if food.is_claimed:
            messages.warning(request, "This food has already been claimed.")
        else:
            food.is_claimed = True
            food.save()
            messages.success(request, "Food claimed successfully!")

    return redirect('home')
