from django.contrib import admin
from .models import Products,Order  # Use 'Product' instead of 'Products'

# Register your model
admin.site.register(Products)
admin.site.register(Order)
