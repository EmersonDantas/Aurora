# Generated by Django 2.1.5 on 2019-02-05 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_student_periods'),
        ('schedule', '0003_auto_20190205_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Student'),
        ),
    ]
