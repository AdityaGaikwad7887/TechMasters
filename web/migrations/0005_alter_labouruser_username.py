# Generated by Django 4.2.2 on 2023-11-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_labouruser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labouruser',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
