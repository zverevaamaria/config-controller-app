# Generated by Django 4.1.3 on 2022-11-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0003_remove_config_last_called_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]