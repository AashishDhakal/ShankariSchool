# Generated by Django 3.0.1 on 2020-02-01 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20200201_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('file', models.FileField(upload_to='downloads')),
            ],
        ),
    ]
