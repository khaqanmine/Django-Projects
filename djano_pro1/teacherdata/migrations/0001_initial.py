# Generated by Django 4.0 on 2021-12-17 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='teacherdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.TextField(max_length=100)),
                ('salary', models.IntegerField(max_length=10)),
            ],
        ),
    ]
