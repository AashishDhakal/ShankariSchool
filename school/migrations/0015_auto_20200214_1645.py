# Generated by Django 3.0.3 on 2020-02-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_teammember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='notice_image',
            field=models.ImageField(blank=True, upload_to='notices'),
        ),
    ]
