# Generated by Django 3.2.9 on 2021-11-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_office_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='photo',
        ),
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, upload_to='person_images/'),
        ),
    ]
