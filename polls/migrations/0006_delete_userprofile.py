# Generated by Django 5.0.2 on 2024-07-07 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_userprofile_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
