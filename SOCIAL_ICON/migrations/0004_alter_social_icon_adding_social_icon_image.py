# Generated by Django 4.0.3 on 2022-06-29 11:43

import SOCIAL_ICON.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SOCIAL_ICON', '0003_social_icon_adding_social_icon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_icon_adding',
            name='social_icon_image',
            field=models.ImageField(default=None, help_text='Please use our recommended dimensions: 16 x 16 PX, 10 KB MAX', null=True, upload_to='social_icon/', validators=[SOCIAL_ICON.models.validate_image]),
        ),
    ]