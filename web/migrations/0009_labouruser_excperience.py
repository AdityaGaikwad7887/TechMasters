# Generated by Django 4.2.2 on 2023-11-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_remove_labouruser_excperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='labouruser',
            name='excperience',
            field=models.IntegerField(default=0),
        ),
    ]