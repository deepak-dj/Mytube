# from django.contrib.auth.models import User
# from user.models import Profile
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
#
# @receiver(post_save,sender=User)
#
# def create_profile(sender,created,instance,**kwargs):
#     if created:
#         Profile.objects.create(user = instance)
#
# @receiver(post_save,sender=User)
# def profile_created(sender,instance,**kwargs):
#     instance.profile.save()


##############################

from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)

def profile_save(sender,instance,**kwargs):
    instance.profile.save()