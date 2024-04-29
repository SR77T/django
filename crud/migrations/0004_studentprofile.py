# Generated by Django 5.0.4 on 2024-04-29 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_student_classroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=14)),
                ('bio', models.TextField(max_length=500)),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to='')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crud.student')),
            ],
        ),
    ]
