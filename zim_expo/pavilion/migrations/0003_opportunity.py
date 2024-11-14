# Generated by Django 5.1.3 on 2024-11-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pavilion', '0002_product_comment_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('qualifications', models.TextField()),
                ('contact_details', models.CharField(max_length=255)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['job_title', 'date_posted'],
            },
        ),
    ]