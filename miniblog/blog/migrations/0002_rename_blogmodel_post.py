# Generated by Django 3.2.3 on 2021-06-06 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogmodel',
            new_name='Post',
        ),
    ]
