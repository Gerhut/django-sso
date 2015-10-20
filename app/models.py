from django.db import models

class Entry(models.Model):

    title = models.CharField(max_length=80)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.title
