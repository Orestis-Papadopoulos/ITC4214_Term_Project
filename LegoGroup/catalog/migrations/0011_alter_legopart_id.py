# Generated by Django 4.1.2 on 2022-12-06 19:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legopart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]