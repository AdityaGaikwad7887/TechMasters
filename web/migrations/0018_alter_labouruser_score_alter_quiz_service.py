# Generated by Django 4.2.2 on 2023-11-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_labouruser_user_normaluser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labouruser',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='service',
            field=models.CharField(max_length=50),
        ),
    ]