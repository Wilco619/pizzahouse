# Generated by Django 4.1.7 on 2023-04-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_blog_main_image_alter_blog_other_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flaticon',
            name='icon',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
