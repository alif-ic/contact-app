# Generated by Django 2.2.3 on 2019-07-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20190710_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
