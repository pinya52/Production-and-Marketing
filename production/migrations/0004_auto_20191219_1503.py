# Generated by Django 2.2.5 on 2019-12-19 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_auto_20191219_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firm',
            name='FirmID',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
