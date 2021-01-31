from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Account(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, null=False, primary_key=True, editable=False, unique=True)
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
    country = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    website=models.URLField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.account.username
