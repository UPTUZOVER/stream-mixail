from django.contrib import admin
from .project import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        'status',
        "author_role",
        "created_at",
        "deadline",
        "closed_at",
        'author'
    )
    #exclude = ('created_at', 'closed_at') admin paneldan malumot chiqmasligi uchun
    list_filter = ('status', 'author_role', "created_at", 'deadline', 'closed_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'closed_at')
    ordering = ('-created_at',)