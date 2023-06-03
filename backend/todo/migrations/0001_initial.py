# Generated by Django 4.2.1 on 2023-06-03 08:55

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('due_date', models.DateField(blank=True)),
                ('status', models.CharField(choices=[('O', 'Open'), ('W', 'Working'), ('D', 'Done'), ('v', 'Overdue')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tag', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
