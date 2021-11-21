# Generated by Django 3.2.9 on 2021-11-17 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_dir', models.BooleanField(default=False)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('size', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='filesharing.downloadfilemodel')),
            ],
        ),
    ]
