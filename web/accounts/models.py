from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=False, null=False)


    def __unicode__(self):
        return self.account.username
