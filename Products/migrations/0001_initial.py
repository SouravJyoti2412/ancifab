# Generated by Django 3.2.6 on 2022-07-27 13:43

import Products.models
import autoslug.fields
import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer_login', '0005_singup_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_code', models.CharField(max_length=50)),
                ('product_des', ckeditor.fields.RichTextField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('discount', models.BooleanField(default=False)),
                ('discount_price', models.IntegerField()),
                ('Thrumnil', models.ImageField(help_text='recommended dimensions:800X960px,200 KB MAX', upload_to='products/', validators=[Products.models.validate_image200kb])),
                ('Thrumnil2', models.ImageField(help_text='recommended dimensions:800X960px,200 KB MAX', upload_to='products/', validators=[Products.models.validate_image200kb])),
                ('Image1', models.ImageField(help_text='recommended dimensions:800X960px,200 KB MAX', upload_to='products/', validators=[Products.models.validate_image200kb])),
                ('Image2', models.ImageField(blank=True, help_text='recommended dimensions:800X960px,200 KB MAX', null=True, upload_to='products/', validators=[Products.models.validate_image200kb])),
                ('Image3', models.ImageField(blank=True, help_text='recommended dimensions:800X960px,200 KB MAX', null=True, upload_to='products/', validators=[Products.models.validate_image200kb])),
                ('Image4', models.ImageField(blank=True, help_text='recommended dimensions:800X960px,200 KB MAX', null=True, upload_to='products/', validators=[Products.models.validate_image200kb])),
                ('Image5', models.ImageField(blank=True, help_text='recommended dimensions:800X960px,200 KB MAX', null=True, upload_to='products/', validators=[Products.models.validate_image200kb])),
                ('Image6', models.ImageField(blank=True, help_text='recommended dimensions:800X960px,200 KB MAX', null=True, upload_to='products/', validators=[Products.models.validate_image200kb])),
                ('Meta_name', models.CharField(default=None, max_length=255, null=True)),
                ('Meta_description', models.TextField()),
                ('product_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('active', models.BooleanField(default=True)),
                ('stock', models.BooleanField(default=True)),
                ('trending', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ALlorderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('producttotal', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='orderitem/')),
                ('size', models.CharField(blank=True, default=None, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('Category_name', models.CharField(max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='Category_name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='generalQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('mesege', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('view', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='maincategory',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('Thrmbnil_image', models.ImageField(default=None, help_text='Please we recommended dimensions: 362 X 470px, 100 KB MAX and use tranparent logo', null=True, upload_to='social_icon/', validators=[Products.models.validate_image], verbose_name='Thrumbnil Image (362X470px)')),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='product_return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('Color_name', models.CharField(max_length=20)),
                ('Color_Swatch', models.ImageField(default=None, help_text='Please we recommended dimensions: , 10 KB MAX', null=True, upload_to='color_swatches/', validators=[Products.models.validates_image])),
            ],
        ),
        migrations.CreateModel(
            name='productQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('productname', models.CharField(max_length=100)),
                ('productcode', models.CharField(blank=True, max_length=100, null=True)),
                ('mesege', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('view', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('Size_name', models.CharField(max_length=20)),
                ('Size_mesurment', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Size_chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_des', models.TextField()),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='TotalOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(max_length=30)),
                ('Street_adress', models.TextField()),
                ('town', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=10)),
                ('number', models.CharField(default=None, max_length=10)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('paid', models.BooleanField(default=False)),
                ('gst', models.CharField(max_length=50)),
                ('total', models.CharField(max_length=50)),
                ('shipping', models.CharField(blank=True, default=0, max_length=2, null=True)),
                ('order_id', models.CharField(default=uuid.uuid4, editable=False, max_length=250)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_login.singup')),
                ('orderitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.allorderitem')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('Sub_Category_name', models.CharField(max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='Sub_Category_name', unique=True)),
                ('Category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='Products.category')),
            ],
        ),
        migrations.CreateModel(
            name='productreview',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(default=0)),
                ('review_title', models.CharField(max_length=100)),
                ('messege', models.TextField()),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('Parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.productreview')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.addproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_login.singup')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'product reviews',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Orderplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(max_length=30)),
                ('Street_adress', models.TextField()),
                ('town', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('number', models.IntegerField(default=None)),
                ('data', models.DateField(default=datetime.datetime.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_login.singup')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.addproduct')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='maincategory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Products.maincategory'),
        ),
        migrations.CreateModel(
            name='AllOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(max_length=30)),
                ('Street_adress', models.TextField()),
                ('town', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=10)),
                ('number', models.CharField(default=None, max_length=10)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('paid', models.BooleanField(default=False)),
                ('gst', models.CharField(max_length=50)),
                ('total', models.CharField(max_length=50)),
                ('shipping', models.CharField(blank=True, default=0, max_length=2, null=True)),
                ('order_id', models.CharField(default=uuid.uuid4, editable=False, max_length=250)),
                ('payment_mood', models.CharField(blank=True, max_length=10, null=True)),
                ('Orderplaced', models.BooleanField(default=False)),
                ('shipped', models.BooleanField(default=False)),
                ('out_delivery', models.BooleanField(default=False)),
                ('deliverd', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_login.singup')),
            ],
        ),
        migrations.AddField(
            model_name='allorderitem',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.allorders'),
        ),
        migrations.AddField(
            model_name='allorderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.addproduct'),
        ),
        migrations.AddField(
            model_name='addproduct',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Products.category'),
        ),
        migrations.AddField(
            model_name='addproduct',
            name='color',
            field=models.ManyToManyField(related_name='color', to='Products.ProductColor'),
        ),
        migrations.AddField(
            model_name='addproduct',
            name='main_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Products.maincategory'),
        ),
        migrations.AddField(
            model_name='addproduct',
            name='size',
            field=models.ManyToManyField(related_name='size', to='Products.ProductSize'),
        ),
        migrations.AddField(
            model_name='addproduct',
            name='sub_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Products.sub_category'),
        ),
        migrations.CreateModel(
            name='add_to_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('cartProduct', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Products.addproduct')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_login.singup')),
            ],
        ),
    ]
