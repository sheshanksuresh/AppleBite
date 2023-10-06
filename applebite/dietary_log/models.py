from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrates = models.FloatField()
    sugars = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name

class DietaryEntry(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.FloatField()
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def total_calories(self):
        return self.food_item.calories * self.quantity
    
    def __str__(self) -> str:
        return f"{self.food_item.name} on {self.date}"
    
