# Generated by Django 3.2.7 on 2021-10-27 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=45)),
                ('introduction', models.CharField(max_length=1000, null=True)),
                ('college', models.CharField(max_length=100, null=True)),
                ('resume_file_url', models.CharField(max_length=2000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'resumes',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.resume')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'skills',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('duty', models.CharField(max_length=100)),
                ('date_of_joining', models.DateField()),
                ('date_of_resigning', models.DateField(null=True)),
                ('in_office', models.BooleanField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.resume')),
            ],
            options={
                'db_table': 'careers',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recommender', models.CharField(max_length=100, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documents.resume')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'applications',
            },
        ),
    ]
