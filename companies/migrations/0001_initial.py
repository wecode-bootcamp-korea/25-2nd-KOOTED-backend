# Generated by Django 3.2.7 on 2021-10-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.TextField(max_length=5000)),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
                ('employee_number', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='JobGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'job_groups',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=2000)),
                ('job_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.jobgroup')),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='CompanyTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.tag')),
            ],
            options={
                'db_table': 'companies_tags',
            },
        ),
        migrations.CreateModel(
            name='CompanyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
            options={
                'db_table': 'company_images',
            },
        ),
    ]
