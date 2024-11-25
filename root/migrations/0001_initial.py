# Generated by Django 5.1.3 on 2024-11-24 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='default.jpg', upload_to='picture')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('agent_description', models.TextField()),
                ('description', models.TextField()),
                ('client', models.CharField(max_length=200)),
                ('project_date', models.DateTimeField(auto_now_add=True)),
                ('project_url', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.agent')),
                ('category', models.ManyToManyField(to='root.category')),
            ],
        ),
    ]
