# Generated by Django 4.0.3 on 2022-07-02 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_login', '0003_alter_singup_options'),
        ('userinterphase', '0017_alter_blogcomment_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('blog_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinterphase.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_login.singup')),
            ],
        ),
    ]
