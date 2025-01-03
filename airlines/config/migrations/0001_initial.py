# Generated by Django 4.2.4 on 2024-12-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_and_conditions', models.FileField(blank=True, upload_to='terms_and_conditions/')),
                ('email_contact', models.CharField(blank=True, max_length=200, null=True)),
                ('contract', models.FileField(blank=True, upload_to='contract/')),
            ],
        ),
    ]
