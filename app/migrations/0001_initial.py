# Generated by Django 4.2.4 on 2023-08-03 02:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=150)),
                ('date', models.DateTimeField(max_length=400)),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='eventimages')),
                ('is_liked', models.BooleanField(default=False)),
                ('liked_by_users', models.ManyToManyField(blank=True, related_name='liked_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]