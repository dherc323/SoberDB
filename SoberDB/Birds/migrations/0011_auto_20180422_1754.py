# Generated by Django 2.0.2 on 2018-04-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Birds', '0010_auto_20180422_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='BirdPic',
            field=models.FileField(blank=True, default='No image', upload_to=''),
        ),
        migrations.AlterField(
            model_name='finch',
            name='Spectograms',
            field=models.FileField(blank=True, default='No image', upload_to=''),
        ),
    ]
