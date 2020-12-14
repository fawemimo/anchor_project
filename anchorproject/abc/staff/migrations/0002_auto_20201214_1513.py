# Generated by Django 3.1.4 on 2020-12-14 15:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_profile',
            name='time',
        ),
        migrations.AddField(
            model_name='staff_profile',
            name='work_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 15, 13, 51, 307472, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='staff_profile',
            name='work_title',
            field=models.CharField(default='my work', max_length=200),
        ),
        migrations.AddField(
            model_name='staff_profile',
            name='work_to',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 15, 13, 51, 307537, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staff_profile',
            name='staff_id',
            field=models.CharField(blank=True, default='ANC130324', max_length=7, null=True),
        ),
    ]
