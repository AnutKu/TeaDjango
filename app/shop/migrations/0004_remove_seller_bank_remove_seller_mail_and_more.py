# Generated by Django 4.2 on 2023-05-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_seller_alter_names_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='payment_account',
        ),
        migrations.AlterField(
            model_name='names',
            name='seller',
            field=models.CharField(max_length=50),
        ),
    ]
