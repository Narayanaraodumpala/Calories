# Generated by Django 3.0 on 2020-12-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieapp', '0005_auto_20201209_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodmodel',
            name='calories',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='carbohydrates',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='fats',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='minerals',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='protein',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='vitamin',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='foodmodel',
            name='water',
            field=models.FloatField(null=True),
        ),
    ]
