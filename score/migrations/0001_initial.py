# Generated by Django 4.1.1 on 2022-09-19 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('idUser', models.BigIntegerField()),
                ('score', models.BigIntegerField()),
                ('karma', models.IntegerField()),
                ('timePlayed', models.BigIntegerField()),
                ('deaths', models.IntegerField()),
                ('attempt', models.IntegerField()),
                ('decisions', models.TextField()),
                ('updateAt', models.DateTimeField(auto_now=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]