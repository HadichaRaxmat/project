# Generated by Django 5.1.4 on 2024-12-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
