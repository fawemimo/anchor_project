# Generated by Django 3.1.4 on 2020-12-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0033_auto_20201223_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffprofile',
            name='staff_id',
            field=models.CharField(blank=True, default='ANC130683', max_length=10, null=True),
        ),
    ]
