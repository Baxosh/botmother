# Generated by Django 3.1.1 on 2021-10-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botmother', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='stopped_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]