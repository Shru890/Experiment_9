# Generated by Django 3.0.1 on 2021-05-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0006_registerdonor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tdr',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
