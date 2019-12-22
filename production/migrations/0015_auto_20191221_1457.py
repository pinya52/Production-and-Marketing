# Generated by Django 2.2.5 on 2019-12-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0014_auto_20191221_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='made',
            name='mTime',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='oTime',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='provideequip',
            name='peTime',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='providestock',
            name='psTime',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together={('sName', 'Expired')},
        ),
    ]