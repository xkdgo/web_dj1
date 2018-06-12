# Generated by Django 2.0.6 on 2018-06-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('article', models.CharField(max_length=63)),
                ('count', models.IntegerField(default=0)),
                ('arrived', models.DateTimeField()),
            ],
        ),
    ]
