# Generated by Django 5.0.3 on 2024-03-07 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
