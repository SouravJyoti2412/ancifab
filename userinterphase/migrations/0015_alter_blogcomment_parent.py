# Generated by Django 4.0.3 on 2022-07-01 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userinterphase', '0014_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='Parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userinterphase.blogcomment'),
        ),
    ]