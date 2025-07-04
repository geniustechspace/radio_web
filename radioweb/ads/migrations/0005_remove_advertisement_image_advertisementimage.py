# Generated by Django 5.2.1 on 2025-05-30 14:01

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_advertisement_image'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='image',
        ),
        migrations.CreateModel(
            name='AdvertisementImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_text', models.CharField(blank=True, max_length=255)),
                ('advertisement', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ads.advertisement')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
            ],
        ),
    ]
