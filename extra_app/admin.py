from import_export import resources

from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from extra_app.models import DataFullstack, SalaryLevel, SalaryPart


# Register your models here.

class DataFullstackResource(resources.ModelResource):
    class Meta:
        model = DataFullstack


class DataFullstackAdmin(ImportExportActionModelAdmin):
    resource_class = DataFullstackResource
    list_display = [field.name for field in DataFullstack._meta.fields if field.name != 'id']


admin.site.register(DataFullstack, DataFullstackAdmin)


class SalaryLevelResource(resources.ModelResource):
    class Meta:
        model = SalaryLevel


class SalaryLevelAdmin(ImportExportActionModelAdmin):
    resource_class = SalaryLevelResource
    list_display = [field.name for field in SalaryLevel._meta.fields if field.name != 'id']


admin.site.register(SalaryLevel, SalaryLevelAdmin)


class SalaryPartResource(resources.ModelResource):
    class Meta:
        model = SalaryPart


class SalaryPartAdmin(ImportExportActionModelAdmin):
    resource_class = SalaryPartResource
    list_display = [field.name for field in SalaryPart._meta.fields if field.name != 'id']


admin.site.register(SalaryPart, SalaryPartAdmin)
