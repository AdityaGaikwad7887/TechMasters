# Generated by Django 4.2.2 on 2023-11-12 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_alter_labouruser_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='labouruser',
            name='image',
            field=models.ImageField(default='../media/defualtuser.jpg', upload_to='img/%y'),
        ),
    ]
