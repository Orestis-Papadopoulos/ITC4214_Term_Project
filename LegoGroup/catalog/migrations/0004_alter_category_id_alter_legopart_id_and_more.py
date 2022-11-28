# Generated by Django 4.1.2 on 2022-11-28 20:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_user_id_legopart_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='legopart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(choices=[('D', 'Decorated'), ('M', 'Modified'), ('P', 'Promotional'), ('R', 'Round'), ('A', 'Axle'), ('B', 'Brick'), ('C', 'Connector'), ('D', 'Disk'), ('G', 'Gear'), ('B', 'Battery box'), ('P', 'Programmable'), ('L', 'Lights'), ('M', 'Motor'), ('W', 'Wire')], help_text='Select subcategory', max_length=50, unique=True),
        ),
    ]
