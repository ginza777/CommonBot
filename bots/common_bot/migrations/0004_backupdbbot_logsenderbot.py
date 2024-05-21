# Generated by Django 4.2.7 on 2024-05-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_bot', '0003_bottoken_created_at_bottoken_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackupDbBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.CharField(max_length=255, unique=True)),
                ('bot_username', models.CharField(blank=True, max_length=125, null=True)),
                ('channel_name', models.CharField(blank=True, max_length=255, null=True)),
                ('channel_id', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extra_field', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'BackupDb',
                'verbose_name_plural': 'BackupDb',
            },
        ),
        migrations.CreateModel(
            name='LogSenderBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.CharField(max_length=255, unique=True)),
                ('bot_username', models.CharField(blank=True, max_length=125, null=True)),
                ('channel_name', models.CharField(blank=True, max_length=255, null=True)),
                ('channel_id', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extra_field', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'LogBot',
                'verbose_name_plural': 'LogBot',
            },
        ),
    ]