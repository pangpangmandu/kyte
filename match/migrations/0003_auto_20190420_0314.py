# Generated by Django 2.2 on 2019-04-19 18:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_auto_20190420_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='maxPlayer',
            field=models.PositiveSmallIntegerField(default=2, max_length=12),
        ),
        migrations.AlterField(
            model_name='game',
            name='gamename',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.FloatField(default=0.0, max_length=10.0)),
                ('recentUpdate', models.DateField(default=django.utils.timezone.now)),
                ('gameId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='match.Game')),
            ],
        ),
    ]
