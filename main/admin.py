from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Order)
admin.site.register(OrderItem)