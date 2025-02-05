# Generated by Django 5.0.6 on 2024-07-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_coffe_delete_cofe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=111)),
                ('short_description', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('created_date', models.DateField()),
            ],
        ),
    ]
