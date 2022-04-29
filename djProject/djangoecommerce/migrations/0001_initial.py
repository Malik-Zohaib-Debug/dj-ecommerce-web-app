# Generated by Django 3.2.7 on 2022-04-29 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=15)),
                ('email_address', models.EmailField(max_length=30)),
                ('user_address', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('phone_number', models.BigIntegerField()),
                ('user_zip', models.IntegerField()),
            ],
        ),
    ]
