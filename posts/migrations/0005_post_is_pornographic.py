# Generated by Django 3.0.8 on 2020-08-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200820_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_pornographic',
            field=models.BooleanField(default=False),
        ),
    ]
