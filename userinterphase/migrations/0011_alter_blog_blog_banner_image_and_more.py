# Generated by Django 4.0.3 on 2022-06-30 06:27

from django.db import migrations, models
import userinterphase.models


class Migration(migrations.Migration):

    dependencies = [
        ('userinterphase', '0010_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Blog_banner_Image',
            field=models.ImageField(help_text='Please use our recommended dimensions: 868x510px, 150 KB MAX', upload_to='Blog_image/', validators=[userinterphase.models.validate_image], verbose_name='Blog Banner Image(868x510px)'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Blog_first_Image',
            field=models.ImageField(help_text='Please use our recommended dimensions: 8424x300px, 100 KB MAX', upload_to='Blog_image/', validators=[userinterphase.models.validate_images], verbose_name='Blog Banner Image(868x510px)'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Blog_second_Image',
            field=models.ImageField(help_text='Please use our recommended dimensions: 8424x300px, 100 KB MAX', upload_to='Blog_image/', validators=[userinterphase.models.validate_images], verbose_name='Blog Banner Image(868x510px)'),
        ),
    ]
