# Generated by Django 2.0.2 on 2018-04-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=200)),
                ('Room', models.CharField(max_length=200)),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
