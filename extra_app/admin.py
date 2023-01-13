from import_export import resources

from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from extra_app.models import DataFullstack, SalaryLevel, SalaryPart, TopSkills2015, TopSkills2016, TopSkills2017, TopSkills2018, TopSkills2019, TopSkills2020, TopSkills2021, TopSkills2022


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


class TopSkills2015Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2015


class TopSkills2015Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2015Resource
    list_display = [field.name for field in TopSkills2015._meta.fields if field.name != 'id']


admin.site.register(TopSkills2015, TopSkills2015Admin)


class TopSkills2016Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2016


class TopSkills2016Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2016Resource
    list_display = [field.name for field in TopSkills2016._meta.fields if field.name != 'id']


admin.site.register(TopSkills2016, TopSkills2016Admin)


class TopSkills2017Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2017


class TopSkills2017Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2017Resource
    list_display = [field.name for field in TopSkills2017._meta.fields if field.name != 'id']


admin.site.register(TopSkills2017, TopSkills2017Admin)


class TopSkills2018Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2018


class TopSkills2018Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2018Resource
    list_display = [field.name for field in TopSkills2018._meta.fields if field.name != 'id']


admin.site.register(TopSkills2018, TopSkills2018Admin)


class TopSkills2019Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2019


class TopSkills2019Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2019Resource
    list_display = [field.name for field in TopSkills2019._meta.fields if field.name != 'id']


admin.site.register(TopSkills2019, TopSkills2019Admin)


class TopSkills2020Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2020


class TopSkills2020Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2020Resource
    list_display = [field.name for field in TopSkills2020._meta.fields if field.name != 'id']


admin.site.register(TopSkills2020, TopSkills2020Admin)


class TopSkills2021Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2021


class TopSkills2021Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2021Resource
    list_display = [field.name for field in TopSkills2021._meta.fields if field.name != 'id']


admin.site.register(TopSkills2021, TopSkills2021Admin)


class TopSkills2022Resource(resources.ModelResource):
    class Meta:
        model = TopSkills2022


class TopSkills2022Admin(ImportExportActionModelAdmin):
    resource_class = TopSkills2022Resource
    list_display = [field.name for field in TopSkills2022._meta.fields if field.name != 'id']


admin.site.register(TopSkills2022, TopSkills2022Admin)