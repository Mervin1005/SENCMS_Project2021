# Generated by Django 3.2.8 on 2021-10-31 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articles_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='tag',
            field=models.TextField(default=''),
        ),
    ]
