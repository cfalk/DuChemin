from django.db import models
from django.contrib.auth.models import User
from duchemin.models.piece import DCPiece
from duchemin.models.analysis import DCAnalysis
from duchemin.models.reconstruction import DCReconstruction


class DCUserProfile(models.Model):
    class Meta:
        app_label = "duchemin"

    user = models.OneToOneField(User)
    favourited_piece = models.ManyToManyField(DCPiece)
    favourited_analysis = models.ManyToManyField(DCAnalysis)
    favourited_reconstruction = models.ManyToManyField(DCReconstruction)
