# Generated by Django 3.1.1 on 2020-09-24 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200924_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoinment',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='appoinment',
            name='treatment',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Appoinment',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Treatment',
        ),
    ]