# Generated by Django 2.2.24 on 2022-03-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0203_auto_20220324_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bounty',
            name='ressources',
        ),
        migrations.AddField(
            model_name='bounty',
            name='resources',
            field=models.TextField(blank=True, default='', help_text='Resources'),
        ),
    ]