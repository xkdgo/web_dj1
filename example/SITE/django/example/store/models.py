from django.db import models

# Create your models here.
class Tovar(models.Model):

    title = models.CharField(max_length=255)
    article = models.CharField(max_length=63)
    count = models.IntegerField(default=0)
    arrived = models.DateTimeField()

    @property
    def full_title(self):
        return '{0.title} ({0.article})'.format(self)

    def __str__(self):
        return '({0.article}).{0.title}'.format(self)


