# Generated by Django 4.1 on 2023-08-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testcase_name', models.CharField(max_length=50, unique=True)),
                ('testcase_text', models.CharField(max_length=100, unique=True)),
                ('testcase_level', models.IntegerField(default=0)),
            ],
        ),
    ]
