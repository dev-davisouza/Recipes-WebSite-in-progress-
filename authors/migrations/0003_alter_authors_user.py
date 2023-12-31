# Generated by Django 4.2.2 on 2023-12-14 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authors', '0002_alter_authors_email_alter_authors_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
