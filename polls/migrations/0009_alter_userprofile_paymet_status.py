# Generated by Django 5.0.2 on 2024-07-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_userprofile_paymet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='paymet_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
