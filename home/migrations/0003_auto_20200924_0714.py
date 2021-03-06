# Generated by Django 3.1.1 on 2020-09-24 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200924_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='appoinment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.patient'),
        ),
        migrations.AddField(
            model_name='appoinment',
            name='treatment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.treatment'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
