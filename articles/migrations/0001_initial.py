# Generated by Django 3.0.7 on 2020-06-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_header', models.CharField(max_length=250)),
                ('article_body', models.TextField()),
            ],
        ),
    ]
