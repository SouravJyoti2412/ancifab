# Generated by Django 3.2.6 on 2022-07-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_returnallorders_returnordersitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='returnallorders',
            name='address',
            field=models.TextField(default=None),
        ),
    ]