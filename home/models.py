# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    password = models.TextField(max_length=255, null=True, blank=True)
    group = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Project(models.Model):

    #__Project_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Task(models.Model):

    #__Task_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(blank=True, null=True, default=timezone.now)
    stop = models.DateTimeField(blank=True, null=True, default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    #__Task_FIELDS__END

    class Meta:
        verbose_name        = _("Task")
        verbose_name_plural = _("Task")


class Produkt(models.Model):

    #__Produkt_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Produkt_FIELDS__END

    class Meta:
        verbose_name        = _("Produkt")
        verbose_name_plural = _("Produkt")



#__MODELS__END
