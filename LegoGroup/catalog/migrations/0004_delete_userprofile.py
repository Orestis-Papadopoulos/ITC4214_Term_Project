# Generated by Django 4.1.2 on 2022-12-08 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_userprofile_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
