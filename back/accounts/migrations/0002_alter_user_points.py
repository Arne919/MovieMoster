# Generated by Django 4.2.16 on 2024-11-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.IntegerField(default=500),
        ),
    ]