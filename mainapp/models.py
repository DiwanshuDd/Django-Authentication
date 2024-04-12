from django.db import models
from functools import partial
from django.contrib.auth.models import User

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.crypto import get_random_string


make_stream_key = partial(get_random_string, 20)


class Stream(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="stream", on_delete=models.CASCADE)
    key = models.CharField(max_length=20, default=make_stream_key, unique=True)
    started_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def is_live(self):
        return self.started_at is not None

    @property
    def hls_url(self):
        return reverse("hls-url", args=(self.user.username,))


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="create_stream_for_user")
def create_stream_for_user(sender, instance=None, created=False, **kwargs):
    """ Create a stream for new users.
    """
    if created:
        Stream.objects.create(user=instance)
class MyExistingModel(models.Model):
    name = models.CharField(max_length=100)
    # Other fields and methods for your existing model
 
# New models for authentication functionalities
class LoginLog(models.Model):
    user = models.ForeignKey(MyExistingModel, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    # Other fields for login logging
 
class PasswordResetRequest(models.Model):
    user = models.ForeignKey(MyExistingModel, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    requested_at = models.DateTimeField(auto_now_add=True)
    # Other fields for password reset request
class Camera(models.Model):
    name = models.CharField(max_length=100)
 

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
class Employee(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as required

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=True)

    class Meta:
        unique_together = ('employee', 'date')
class EmployeeAttendance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()



