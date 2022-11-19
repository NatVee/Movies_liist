from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=50)
    year = models.IntegerField(default=None)

    class Meta:
        get_latest_by = 'id'

    def __str__(self):
        return self.title
