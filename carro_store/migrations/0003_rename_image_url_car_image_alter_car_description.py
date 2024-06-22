# Generated by Django 5.0.6 on 2024-06-22 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro_store', '0002_car_image_url_alter_dueño_cédula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='image_url',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
