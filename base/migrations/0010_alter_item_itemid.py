# Generated by Django 4.2.2 on 2023-06-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_order_rename_cat_item_category_alter_item_itemid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemId',
            field=models.IntegerField(),
        ),
    ]