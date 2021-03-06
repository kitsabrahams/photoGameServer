# Generated by Django 2.1 on 2018-08-11 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20180811_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='votinghistory',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votinghistory',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
