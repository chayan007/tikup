# Generated by Django 3.0.8 on 2020-09-23 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0006_auto_20200915_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sounds.SoundCategory'),
        ),
    ]
