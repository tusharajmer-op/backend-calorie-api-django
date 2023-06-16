# Generated by Django 4.2.2 on 2023-06-16 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50, unique=True)),
                ('FirstName', models.CharField(max_length=50)),
                ('LasttName', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=250)),
                ('is_staff', models.BooleanField(default=False)),
                ('CreatedOn', models.DateField(auto_now=True)),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertype')),
            ],
        ),
    ]
