# Generated by Django 5.0.2 on 2024-07-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_remove_statereview_user_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_user_history',
            name='Submition_title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review_user_history',
            name='file',
            field=models.FileField(null=True, upload_to='Review_file/'),
        ),
        migrations.AlterField(
            model_name='review_user_history',
            name='status_review',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
