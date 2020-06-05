"""
Creating Model to represent a table in Django
"""
from django.db import models
from django.contrib.auth.models import User


class ActivityPeriod(models.Model):
    """

    """
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
