# Generated by Django 2.0.2 on 2018-05-10 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Birds', '0012_auto_20180510_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finch',
            name='Alive',
            field=models.BooleanField(),
        ),
    ]
