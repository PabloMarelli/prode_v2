# Generated by Django 4.0.5 on 2022-06-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prode', '0012_forecast_created_at_forecast_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='match_end',
        ),
        migrations.AddField(
            model_name='match',
            name='duration_mins',
            field=models.IntegerField(default=90),
        ),
    ]