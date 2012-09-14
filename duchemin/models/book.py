from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class DCBook(models.Model):
    class Meta:
        app_label = "duchemin"
        verbose_name = "Book"
        verbose_name_plural = "Books"

    book_id = models.CharField(max_length=16, unique=True)
    title = models.CharField(max_length=128, blank=True)
    complete_title = models.CharField(max_length=128, blank=True)
    publisher = models.CharField(max_length=64, blank=True)
    place_publication = models.CharField(max_length=64, blank=True)
    date = models.CharField(max_length=64, blank=True)
    volumes = models.CharField(max_length=64, blank=True)
    part_st_id = models.CharField(max_length=16, blank=True)
    part_tb_id = models.CharField(max_length=16, blank=True)
    num_compositions = models.CharField(max_length=16, blank=True)
    num_pages = models.CharField(max_length=16, blank=True)
    location = models.CharField(max_length=16, blank=True)
    rism = models.CharField(max_length=16, blank=True)
    cesr = models.CharField(max_length=16, blank=True)
    remarks = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return "{0}".format(self.title)
