from django.contrib import admin
from .models import Circle

class CircleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner']
    search_fields = ['name']

    class Meta:
        model = Circle

admin.site.register(Circle, CircleAdmin)