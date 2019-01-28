# Generated by Django 2.1.5 on 2019-01-28 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190128_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.User')),
                ('ies', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('year_graduation', models.IntegerField()),
            ],
            bases=('user.user',),
        ),
    ]
