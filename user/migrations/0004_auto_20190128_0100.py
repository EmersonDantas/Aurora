# Generated by Django 2.1.5 on 2019-01-28 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190128_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
