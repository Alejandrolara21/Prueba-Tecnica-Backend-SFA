# Generated by Django 3.2.16 on 2022-12-26 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0001_initial'),
        ('users', '0004_auto_20221225_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='states.state'),
            preserve_default=False,
        ),
    ]
