<<<<<<< HEAD
# Generated by Django 3.0.1 on 2020-02-09 14:10
=======
# Generated by Django 3.0.3 on 2020-02-09 14:14
>>>>>>> 7b215a7adc956b4b5b7d7ab69953ab271113c593

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20200201_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('preloader', models.ImageField(upload_to='preloader')),
                ('background_image', models.ImageField(upload_to='background')),
                ('logo', models.ImageField(upload_to='logo')),
=======
                ('preloader', models.ImageField(blank=True, upload_to='preloader')),
                ('background_image', models.ImageField(blank=True, upload_to='background')),
                ('logo', models.ImageField(blank=True, upload_to='logo')),
>>>>>>> 7b215a7adc956b4b5b7d7ab69953ab271113c593
            ],
            options={
                'verbose_name': 'Homepage',
                'verbose_name_plural': 'Homepage',
            },
        ),
    ]
