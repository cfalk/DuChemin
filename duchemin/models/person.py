from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class DCPerson(models.Model):
    class Meta:
        app_label = "duchemin"
        verbose_name = "Person"
        verbose_name_plural = "People"

    person_id = models.CharField(max_length=16, unique=True, null=True)
    surname = models.CharField(max_length=64, blank=True, null=True)
    given_name = models.CharField(max_length=64, blank=True, null=True)
    birth_date = models.CharField(max_length=16, blank=True, null=True)
    death_date = models.CharField(max_length=16, blank=True, null=True)
    active_date = models.CharField(max_length=16, blank=True, null=True)
    alt_spelling = models.CharField(max_length=64, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"{0}, {1}".format(self.surname, self.given_name)
