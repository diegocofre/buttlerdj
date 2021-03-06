# Generated by Django 3.0.6 on 2020-05-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20200504_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='end_confirm',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segment',
            name='end_message',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
