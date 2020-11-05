from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.budget}'


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.title}: Price {self.price}'
