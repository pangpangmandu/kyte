# Generated by Django 2.2 on 2019-04-19 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='introduction',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='N/A', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='running',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='signUpDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='steamid',
            field=models.CharField(default='N/A', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ranking',
            field=models.CharField(max_length=20),
        ),
    ]