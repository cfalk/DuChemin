from django.db import models

from duchemin.models.book import DCBook
from duchemin.models.person import DCPerson
from duchemin.models.file import DCFile


class DCPiece(models.Model):
    class Meta:
        app_label = "duchemin"
        verbose_name = "Piece"
        verbose_name_plural = "Pieces"

    piece_id = models.CharField(max_length=16, unique=True, db_index=True)
    book_id = models.ForeignKey(DCBook, to_field='book_id')
    book_position = models.IntegerField(max_length=16, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    composer_id = models.ForeignKey(DCPerson, to_field='person_id')
    composer_src = models.CharField(max_length=64, blank=True, null=True)
    forces = models.CharField(max_length=16, blank=True, null=True)
    print_concordances = models.CharField(max_length=128, blank=True, null=True)
    ms_concordances = models.CharField(max_length=128, blank=True, null=True)
    attachments = models.ManyToManyField(DCFile, blank=True, null=True)

    def __unicode__(self):
        return u"{0}".format(self.title)
