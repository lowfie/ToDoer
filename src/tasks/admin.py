from django.contrib import admin

from src.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
