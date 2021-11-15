from django.contrib import admin
from . import models


# for multiple addition records
class StudentsInlineAdmin(admin.StackedInline):
    model = models.Students
    extra = 2


@admin.register(models.Students)
class StudentsAdmin(admin.ModelAdmin):
    model = models.Students
    ordering = ['first_name']
    readonly_fields = ('id', 'enroll_date')


@admin.register(models.Fields)
class FieldsAdmin(admin.ModelAdmin):
    ordering = ['field_name']
    inlines = [StudentsInlineAdmin, ]


@admin.register(models.Courses)
class CoursesAdmin(admin.ModelAdmin):
    ordering = ['course_name']
