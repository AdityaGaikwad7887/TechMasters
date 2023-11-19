# Generated by Django 4.2.2 on 2023-11-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/%y')),
                ('caption', models.CharField(max_length=20)),
                ('charges', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/%y')),
                ('caption', models.CharField(max_length=20)),
                ('charges', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]