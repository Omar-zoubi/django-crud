# Generated by Django 3.2.4 on 2021-06-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='reviewer',
            new_name='purcheser',
        ),
        migrations.RenameField(
            model_name='snack',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='snack',
            name='rating',
        ),
        migrations.AddField(
            model_name='snack',
            name='description',
            field=models.TextField(default=0),
        ),
    ]
