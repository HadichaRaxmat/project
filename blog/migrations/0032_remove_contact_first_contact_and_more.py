# Generated by Django 5.1.4 on 2024-12-14 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_alter_popular_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='first_contact',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='fourth_contact',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='second_contact',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='third_contact',
        ),
    ]