# Generated by Django 4.1.6 on 2023-02-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/'),
        ),
    ]