# Generated by Django 3.1.5 on 2021-01-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
