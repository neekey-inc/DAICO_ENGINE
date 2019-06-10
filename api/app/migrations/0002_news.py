# Generated by Django 2.1 on 2019-06-09 09:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='media/')),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
