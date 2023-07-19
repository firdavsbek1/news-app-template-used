from django.db.models.signals import post_save,post_delete
from .models import Profile,User


def create_profile(sender,instance,created,**kwargs):
    if created:
        user=instance
        profile = Profile.objects.create(
            user=user,
            name=user.first_name+" "+ user.last_name,
            username=user.username,
            email=user.email,
        )


def update_user(sender,instance,created,**kwargs):
    if not created:
        profile = instance
        profile.user.username=profile.username
        profile.user.email = profile.email
        profile.user.save()


post_save.connect(create_profile,sender=User)
post_save.connect(update_user,sender=Profile)