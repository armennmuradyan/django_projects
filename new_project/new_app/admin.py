from django.contrib import admin
from new_app.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status")
    fields = ("name", "status", 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Task, TaskAdmin)