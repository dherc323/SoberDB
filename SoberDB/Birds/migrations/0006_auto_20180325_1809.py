# Generated by Django 2.0.2 on 2018-03-25 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Birds', '0005_auto_20180325_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='Notes',
            field=models.TextField(default='No notes'),
        ),
        migrations.AddField(
            model_name='finch',
            name='Origin',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
