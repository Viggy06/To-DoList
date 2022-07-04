from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',) #to display hidden var as read only 

# Register your models here.

admin.site.register(Todo, TodoAdmin)