# Generated by Django 5.0.3 on 2024-03-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('lng', models.CharField(max_length=20)),
                ('lat', models.CharField(max_length=20)),
            ],
        ),
    ]
