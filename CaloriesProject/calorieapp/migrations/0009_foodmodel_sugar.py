# Generated by Django 3.0 on 2020-12-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieapp', '0008_remove_foodmodel_minerals'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmodel',
            name='sugar',
            field=models.FloatField(null=True),
        ),
    ]
