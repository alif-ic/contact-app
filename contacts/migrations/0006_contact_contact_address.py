# Generated by Django 2.2.3 on 2019-07-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20190710_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_address',
            field=models.TextField(default='', max_length=120),
        ),
    ]
