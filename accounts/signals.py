from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=get_user_model())
def assign_special_permission(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename="special_status")
        instance.user_permissions.add(permission)
