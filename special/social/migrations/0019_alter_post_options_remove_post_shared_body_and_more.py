# Generated by Django 4.2.7 on 2024-03-01 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0018_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='shared_body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='shared_on',
        ),
        migrations.RemoveField(
            model_name='post',
            name='shared_user',
        ),
    ]
