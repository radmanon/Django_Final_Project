# Generated by Django 4.0 on 2021-12-31 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_is_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/resume/', verbose_name='عکس رزومه'),
        ),
    ]
