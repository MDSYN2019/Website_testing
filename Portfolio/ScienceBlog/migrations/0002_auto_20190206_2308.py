# Generated by Django 2.1.5 on 2019-02-06 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScienceBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='science',
            old_name='lab_involvment',
            new_name='lab_involvement',
        ),
    ]
