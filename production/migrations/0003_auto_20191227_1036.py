# Generated by Django 2.2.5 on 2019-12-27 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_auto_20191227_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='made',
            old_name='mID',
            new_name='madeID',
        ),
    ]
