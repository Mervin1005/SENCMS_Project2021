# Generated by Django 3.2.8 on 2021-10-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('catname', models.CharField(max_length=50)),
                ('catid', models.IntegerField()),
            ],
        ),
    ]