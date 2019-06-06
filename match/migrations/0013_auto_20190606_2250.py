# Generated by Django 2.2 on 2019-06-06 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0012_auto_20190606_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='steamid',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='gameId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.Game'),
        ),
        migrations.AlterField(
            model_name='review',
            name='gameId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.Game'),
        ),
    ]
