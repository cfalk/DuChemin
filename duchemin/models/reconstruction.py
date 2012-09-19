from django.db import models


class DCReconstruction(models.Model):
    class Meta:
        app_label = "duchemin"
        verbose_name = "Reconstruction"
        verbose_name_plural = "Reconstructions"
