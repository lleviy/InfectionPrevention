# Generated by Django 3.1.2 on 2020-10-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='danger_level',
            field=models.FloatField(default=0.6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]