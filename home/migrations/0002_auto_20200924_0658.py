# Generated by Django 3.1.1 on 2020-09-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Examination', 'Examination'), ('Undertaking Treatment', 'Undertaking Treatment'), ('Discharged', 'Discharged')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('cost', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('category 1', 'category 1'), ('category 2', 'category 2'), ('category 3', 'category 3')], max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='consultation_name',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='patientstatus',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='patientstatus',
            name='product',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.DeleteModel(
            name='allocation',
        ),
        migrations.DeleteModel(
            name='Consultation_name',
        ),
        migrations.DeleteModel(
            name='PatientStatus',
        ),
    ]
