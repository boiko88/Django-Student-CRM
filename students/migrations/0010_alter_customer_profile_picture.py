# Generated by Django 4.1.3 on 2022-12-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_customer_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
