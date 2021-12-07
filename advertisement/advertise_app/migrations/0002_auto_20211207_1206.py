# Generated by Django 3.2.9 on 2021-12-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('sdk_version', models.CharField(max_length=100)),
                ('session_id', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
                ('country_code', models.CharField(max_length=100)),
                ('media', models.CharField(choices=[('Ad', 'Advertise'), ('IMP', 'Impression')], max_length=65)),
            ],
        ),
        migrations.DeleteModel(
            name='Sdkversion',
        ),
        migrations.DeleteModel(
            name='Username',
        ),
    ]
