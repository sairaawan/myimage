# Generated by Django 3.0.5 on 2020-12-09 15:55

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0003_auto_20200623_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='foundation',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('img', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
