from django.contrib import admin
from .models import Project, Task, TaskList, Tag

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created')
    search_fields = ('title', 'description', 'owner__username')
    list_filter = ('created', 'owner')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'list', 'priority', 'created', 'deadline')
    search_fields = ('title', 'description', 'project__title')
    list_filter = ('priority', 'list', 'created', 'deadline')
    filter_horizontal = ('tags',)


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    search_fields = ('name', 'project__title')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
