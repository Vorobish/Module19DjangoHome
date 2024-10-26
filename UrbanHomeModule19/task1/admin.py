from django.contrib import admin
from .models import *


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)
    list_filter = ('price')

# python manage.py createsuperuser
# python manage.py shell