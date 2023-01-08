from import_export import resources

from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from extra_app.models import DataFullstack


# Register your models here.

class DataFullstackResource(resources.ModelResource):
    class Meta:
        model = DataFullstack


class DataFullstackAdmin(ImportExportActionModelAdmin):
    resource_class = DataFullstackResource
    list_display = [field.name for field in DataFullstack._meta.fields if field.name != 'id']


admin.site.register(DataFullstack, DataFullstackAdmin)
