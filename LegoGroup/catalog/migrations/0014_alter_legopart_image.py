# Generated by Django 4.1.2 on 2022-12-08 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_category_id_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legopart',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]