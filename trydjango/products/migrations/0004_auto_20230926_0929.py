# Generated by Django 2.1.5 on 2023-09-26 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230926_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.BooleanField(null=True),
        ),
    ]
