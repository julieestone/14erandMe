from django.contrib import admin
from .models import Trail
from .models import Review

# Register your models here.
admin.site.register(Trail)
admin.site.register(Review)