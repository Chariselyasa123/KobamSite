# Generated by Django 3.0.4 on 2020-03-07 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('FM', 'FEMALE')], default=1, max_length=2),
        ),
    ]
