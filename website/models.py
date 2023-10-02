from django.db import models
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class User(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("You must provide an email!")
        if not username:
            raise ValueError("You must provide a username!")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class Project(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    github_link = models.CharField(max_length=100, null=True)
    documentation_link = models.CharField(max_length=100, null=True)
    hosted_link = models.CharField(max_length=100, null=True)