from django.contrib import admin

from .models import Dog, Walk
# Register your models here.

admin.site.register(Dog)
admin.site.register(Walk)