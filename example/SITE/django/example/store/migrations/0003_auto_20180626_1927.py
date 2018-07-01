# Generated by Django 2.0.6 on 2018-06-26 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_group_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Group'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='tags',
            field=models.ManyToManyField(to='store.Tag'),
        ),
    ]