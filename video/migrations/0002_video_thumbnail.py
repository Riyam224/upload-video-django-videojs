# Generated by Django 4.0.4 on 2022-04-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.FileField(default=1, upload_to='thumbnail/'),
            preserve_default=False,
        ),
    ]