# Generated by Django 4.0.3 on 2022-06-28 15:16

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('sub_title', models.CharField(max_length=30)),
                ('content', tinymce.models.HTMLField()),
                ('side_image', models.FileField(null=True, upload_to='')),
                ('content_title', models.CharField(default=None, max_length=30)),
                ('content_des', tinymce.models.HTMLField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='All_banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ABOUT_US_BANNER_1920X464px', models.FileField(upload_to='all_banner_except_home/')),
                ('CONTACT_US_BANNER_1920X464px', models.FileField(upload_to='all_banner_except_home/')),
                ('CART_BANNER_1920X464px', models.FileField(upload_to='all_banner_except_home/')),
                ('CHECKOUT_BANNER_1920X464px', models.FileField(upload_to='all_banner_except_home/')),
                ('REGISTER_BANNER_1920X464px', models.FileField(upload_to='all_banner_except_home/')),
                ('LOGIN_BANNER_1920X464px', models.FileField(upload_to='all_banner_except_home/')),
                ('FAQ_BANNER_1920X464px', models.FileField(upload_to='all_banner_except_home/')),
                ('BLOG_BANNER_1920X464px', models.FileField(upload_to='all_banner_except_home/')),
            ],
        ),
        migrations.CreateModel(
            name='contact_details_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=300)),
                ('side_image_375X230', models.FileField(default=None, upload_to='contact/')),
            ],
        ),
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='home_carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1920X1080px', models.FileField(upload_to='home/home_carousel/')),
                ('small_heading_optional', models.CharField(blank=True, max_length=20)),
                ('big_heading_optional', models.CharField(blank=True, max_length=30)),
                ('offer_optional', models.CharField(blank=True, max_length=50)),
                ('image_button_link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='home_collection_banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMAGE_BIG_LEFT_870X800px', models.ImageField(upload_to='home/home_all_banner/')),
                ('IMAGE_SMALL_FIRST_425X390px', models.ImageField(upload_to='home/home_all_banner/')),
                ('BUTTON_LINK_OF_SMALL_FIRST_IMAGE', models.CharField(max_length=255)),
                ('HEADING_OF_SMALL_FIRST_IMAGE', models.CharField(max_length=30)),
                ('IMAGE_SMALL_SECOND_425X390px', models.ImageField(upload_to='home/home_all_banner/')),
                ('BUTTON_LINK_OF_SMALL_SECOND_IMAGE', models.CharField(max_length=255)),
                ('HEADING_OF_SMALL_SECOND_IMAGE', models.CharField(max_length=30)),
                ('IMAGE_RIGHT_DOWN_870X390px', models.ImageField(upload_to='home/home_all_banner/')),
                ('HEADING_OF_RIGHT_DOWN_IMAGE', models.CharField(max_length=30)),
                ('BUTTON_LINK_OF_IMAGE_RIGHT_DOWN', models.CharField(max_length=255)),
                ('MIDDLE_SIDE_IMAGE_1920X1080px', models.ImageField(upload_to='home/home_all_banner/')),
                ('HEADING_OF_MIDDLE_SIDE_IMAGE', models.CharField(max_length=30)),
                ('BUTTON_LINK_OF_MIDDLE_SIDE_IMAGE', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Return_refund_policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Terms_and_Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]