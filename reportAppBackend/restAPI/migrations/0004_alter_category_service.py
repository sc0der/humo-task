# Generated by Django 3.2.5 on 2021-07-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0003_auto_20210721_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='service',
            field=models.ManyToManyField(to='restAPI.Service'),
        ),
    ]
