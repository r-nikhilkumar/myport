# Generated by Django 4.2.7 on 2023-12-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
