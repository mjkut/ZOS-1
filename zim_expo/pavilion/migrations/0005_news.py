# Generated by Django 5.1.3 on 2024-11-13 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pavilion', '0004_opportunity_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['title', 'date_posted'],
            },
        ),
    ]
