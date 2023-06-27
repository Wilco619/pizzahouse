# Generated by Django 4.1.7 on 2023-04-27 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0008_alter_flaticon_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='item',
            old_name='cat',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='item',
            name='itemId',
            field=models.IntegerField(max_length=10),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='itemId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.item'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]