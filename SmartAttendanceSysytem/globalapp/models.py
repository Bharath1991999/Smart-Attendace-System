from datetime import timedelta, date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    head_shot= models.ImageField(upload_to='profile_images',blank=True)
    test_shot = models.ImageField(upload_to='test_images',blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




# list of dates which is needed for creating the sheet for marking attendance
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2020, 1, 1)
end_dt = date(2020, 1, 7)

dates = daterange(start_dt, end_dt)
dates_list = []

for dt in dates : dates_list.append(dt.strftime("D%dM%mY%y"))

# models code from here, dates_list includes all dates during the semester.

from django.db import models

class NS101(models.Model):
    roll = models.IntegerField()

for date in dates_list:
    NS101.add_to_class(date, models.IntegerField(default = 0))