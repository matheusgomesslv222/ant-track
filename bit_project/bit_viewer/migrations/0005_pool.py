# Generated by Django 5.1 on 2024-08-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bit_viewer', '0004_maquina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
    ]
