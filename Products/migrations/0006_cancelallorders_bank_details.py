# Generated by Django 3.2.6 on 2022-07-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_cancelordersitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancelallorders',
            name='bank_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
