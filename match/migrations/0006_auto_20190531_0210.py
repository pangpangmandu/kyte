# Generated by Django 2.2 on 2019-05-30 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0005_auto_20190420_0325'),
    ]

    operations = [
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
        migrations.CreateModel(
            name='MatchedUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chatroom', models.CharField(max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='match.Profile')),
            ],
        ),
    ]
