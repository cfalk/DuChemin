from django.db import models


class DCContentBlock(models.Model):
    class Meta:
        app_label = 'duchemin'
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

    NEWS = "news"
    FEAT = "featured"
    BLOC = "block"
    CONTENT_TYPE_CHOICES = (
        (NEWS, "News"),
        (FEAT, "Featured Reconstruction"),
        (BLOC, "Front Page Block")
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    published = models.BooleanField()
    content_type = models.CharField(max_length=32, choices=CONTENT_TYPE_CHOICES, default=BLOC)
    position = models.IntegerField(choices=((1, "1"), (2, "2"), (3, "3"), (4, "4")), default=1)

    def __unicode__(self):
        return u"{0}".format(self.title)
