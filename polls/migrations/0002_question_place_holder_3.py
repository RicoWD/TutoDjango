# Generated by Django 5.0.7 on 2024-07-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='place_holder_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
