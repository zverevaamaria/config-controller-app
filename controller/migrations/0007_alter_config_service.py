# Generated by Django 4.1.3 on 2022-11-13 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0006_alter_config_service_alter_config_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='service',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='сервис конфига'),
        ),
    ]