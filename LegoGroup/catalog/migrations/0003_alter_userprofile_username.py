# Generated by Django 4.1.2 on 2022-12-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, help_text='Type username here', max_length=30, primary_key=True, serialize=False),
        ),
    ]
