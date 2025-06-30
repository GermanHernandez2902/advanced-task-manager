from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project, TaskList, Tag

@receiver(post_save, sender=Project)
def create_default_lists_and_tags(sender, instance, created, **kwargs):
    if created:
        default_lists = ['To Do', 'In Progress', 'Done']
        for name in default_lists:
            TaskList.objects.get_or_create(name=name, project=instance)

        # Solo se crean si no existen globalmente
        for tag_name in ['frontend', 'backend', 'urgent', 'design']:
            Tag.objects.get_or_create(name=tag_name)
