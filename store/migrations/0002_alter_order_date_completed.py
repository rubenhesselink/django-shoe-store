# Generated by Django 4.0.4 on 2022-04-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]