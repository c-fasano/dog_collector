from django.contrib import admin

from .models import Dog, Walk, Toy
# Register your models here.

admin.site.register(Dog)
admin.site.register(Walk)
admin.site.register(Toy)