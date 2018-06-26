from django.db import models

# Create your models here.
class Group(models.Model):

    code = models.CharField(max_length=3, null=False, blank=False)
    # параметр null относится к БД. параметр blank отеосится к python
    name = models.CharField(max_length=255, null=False, blank=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return '({0.code}) {0.name}'.format(self)

class Tag(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    deprecated = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name





