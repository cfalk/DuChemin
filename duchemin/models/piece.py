from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from duchemin.models.book import DCBook
from duchemin.models.person import DCPerson


class DCPiece(models.Model):
    class Meta:
        app_label = "duchemin"
        verbose_name = "Piece"
        verbose_name_plural = "Pieces"

    piece_id = models.CharField(max_length=16, unique=True)
    book_id = models.ForeignKey(DCBook, to_field='book_id')
    book_position = models.CharField(max_length=16, blank=True)
    title = models.CharField(max_length=64, blank=True)
    composer_id = models.ForeignKey(DCPerson, to_field='person_id')
    composer_src = models.CharField(max_length=64, blank=True)
    forces = models.CharField(max_length=16, blank=True)
    print_concordances = models.CharField(max_length=128, blank=True)
    ms_concordances = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return u"{0}".format(self.title)
