# Generated by Django 2.0.2 on 2018-03-30 04:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Birds', '0006_auto_20180325_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='Alive',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='finch',
            name='Notes',
            field=models.TextField(default=' No notes added'),
        ),
    ]
