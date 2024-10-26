from django.db import models


class Buyer(models.Model):
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
    buyer = models.ManyToManyField(Buyer, related_name='buyers')


# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# Buyer.objects.create(name='Ilya', balance=1500.05, age=24)
# Game.objects.create(title='Cyberpunk 2077', cost=31, size=46.2, description='Game of the year', age_limited=True)
# Game.objects.get(id=1).buyer.set((1, 2))