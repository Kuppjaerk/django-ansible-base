# Generated by Django 4.2.8 on 2024-04-09 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dab_authentication', '0006_alter_authenticatoruser_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authenticator',
            name='users',
        ),
        migrations.AlterField(
            model_name='authenticatoruser',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='authenticator_provider', to='dab_authentication.authenticator', to_field='slug'),
        ),
    ]
