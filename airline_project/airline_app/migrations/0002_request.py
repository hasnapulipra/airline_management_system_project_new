# Generated by Django 4.1.1 on 2022-11-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('username', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=50)),
                ('contact', models.TextField(max_length=50)),
                ('password', models.TextField(max_length=50)),
                ('country', models.TextField(max_length=50)),
                ('image', models.ImageField(upload_to='pictures/')),
            ],
        ),
    ]
