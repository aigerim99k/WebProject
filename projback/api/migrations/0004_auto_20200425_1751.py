# Generated by Django 3.0.5 on 2020-04-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200425_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]