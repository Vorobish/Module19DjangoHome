from django.db import models


class Bayer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=50000)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=15000)
    size = models.DecimalField(decimal_places=2, max_digits=1024)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Bayer, related_name='buyers')


# python manage.py makemigrations
# python manage.py migrate