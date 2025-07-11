# Generated by Django 5.2.1 on 2025-05-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='media/')),
                ('author', models.CharField(max_length=120)),
                ('text', models.TextField(blank=True, null=True)),
                ('oldPrice', models.FloatField()),
                ('newPrice', models.FloatField()),
                ('count', models.IntegerField()),
                ('date', models.DateField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
