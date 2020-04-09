from django.contrib import admin
# aynı klasörün altına olduğunu göstermek için .
# models in altındaki Todo modelini al
from .models import Todo
# Register your models here.
admin.site.register(Todo)