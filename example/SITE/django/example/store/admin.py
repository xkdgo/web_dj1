from django.contrib import admin

# Register your models here.
from .models import Tovar, Group, Tag

admin.site.register(Tovar)
admin.site.register(Group)
admin.site.register(Tag)

