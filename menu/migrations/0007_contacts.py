# Generated by Django 5.0.6 on 2024-07-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_comment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numb', models.IntegerField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
