# Generated by Django 3.2.19 on 2023-06-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(choices=[('SPORT', 'SPORT'), ('GAMING', 'GAMING'), ('FOOD', 'FOOD'), ('TRAVELING', 'TRAVELING'), ('HOME', 'HOME'), ('ACTIVITIES', 'ACTIVITIES')], default='Sport', max_length=30),
        ),
    ]
