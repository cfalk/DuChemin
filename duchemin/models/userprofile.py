from django.db import models
from django.contrib.auth.models import User
from duchemin.models.piece import DCPiece


class DCUserProfile(models.Model):
    class Meta:
        app_label = "duchemin"

    user = models.OneToOneField(User)
    favourited = models.ManyToManyField(DCPiece)
