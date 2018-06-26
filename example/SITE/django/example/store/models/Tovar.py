from django.db import models
from .Group import Group, Tag

# Create your models here.
class Tovar(models.Model):

    title = models.CharField(max_length=255)
    article = models.CharField(max_length=63)
    count = models.IntegerField(default=0)
    arrived = models.DateTimeField()

    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag)

    @property
    def full_title(self):
        return '{0.title} ({0.article})'.format(self)

    def __str__(self):
        return '({0.article}).{0.title}'.format(self)


