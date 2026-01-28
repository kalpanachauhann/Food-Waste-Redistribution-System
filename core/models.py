from django.db import models

class FoodPost(models.Model):
    restaurant_name = models.CharField(max_length=100)
    food_item = models.CharField(max_length=200)
    quantity = models.IntegerField()
    expiry_time = models.DateTimeField()
    posted_at = models.DateTimeField(auto_now_add=True)
    is_claimed = models.BooleanField(default=False)  # NEW

    def __str__(self):
        return self.food_item
