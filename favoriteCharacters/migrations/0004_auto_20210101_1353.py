# Generated by Django 3.1.4 on 2021-01-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favoriteCharacters', '0003_auto_20201231_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecharacters',
            name='user_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
