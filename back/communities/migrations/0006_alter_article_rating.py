# Generated by Django 4.2.16 on 2024-11-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0005_article_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]