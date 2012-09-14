from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class DCReconstruction(models.Model):
    class Meta:
        app_label = "duchemin"
        verbose_name = "Reconstruction"
        verbose_name_plural = "Reconstructions"
