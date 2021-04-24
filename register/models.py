from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isLibrarian = models.BooleanField()
    def __str__(self):
        return self.user.username + ' Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff == True:
            Profile.objects.create(user=instance,isLibrarian=True)
        else:
            Profile.objects.create(user=instance,isLibrarian=False)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
