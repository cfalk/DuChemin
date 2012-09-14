from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from duchemin.models.piece import DCPiece


class DCPhrase(models.Model):
    class Meta:
        app_label = "duchemin"
        verbose_name = "Phrase"
        verbose_name_plural = "Phrases"

    phrase_id = models.CharField(max_length=16, unique=True)
    piece_id = models.ForeignKey(DCPiece, to_field='piece_id')
    phrase_num = models.CharField(max_length=4, blank=True, null=True)
    phrase_start = models.CharField(max_length=4, blank=True, null=True)
    phrase_stop = models.CharField(max_length=4, blank=True, null=True)
    phrase_text = models.CharField(max_length=255, blank=True, null=True)
    rhyme = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        return u"{0}, {1}".format(self.piece_id.piece_id, self.phrase_num)
