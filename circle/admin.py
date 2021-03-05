from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Circle

class CircleResource(resources.ModelResource):
    class Meta:
        model = Circle
        skip_unchanged = True
        report_skipped = False        

@admin.register(Circle)
class CircleAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'owner']
    search_fields = ['name']
    resource_class = CircleResource


# admin.site.register(Circle, CircleAdmin)