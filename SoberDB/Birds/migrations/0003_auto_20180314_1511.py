# Generated by Django 2.0.2 on 2018-03-14 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Birds', '0002_auto_20180314_1450'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Finches',
            new_name='Finch',
        ),
        migrations.AlterModelOptions(
            name='finch',
            options={'verbose_name_plural': 'Finch'},
        ),
    ]
