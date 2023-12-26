# Generated by Django 5.0 on 2023-12-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educationdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='default', max_length=50)),
                ('college_name', models.CharField(max_length=250)),
                ('degree_name', models.CharField(max_length=50)),
                ('college_start_year', models.CharField(max_length=40)),
                ('college_end_year', models.CharField(max_length=40)),
                ('about_college', models.TextField()),
                ('xii_school_name', models.CharField(max_length=250)),
                ('xii_school_board_name', models.CharField(max_length=50)),
                ('xii_school_start', models.CharField(max_length=40)),
                ('xii_school_end', models.CharField(max_length=40)),
                ('about_xii_school', models.TextField()),
                ('x_school_name', models.CharField(max_length=250)),
                ('x_school_board_name', models.CharField(max_length=50)),
                ('x_school_start', models.CharField(max_length=40)),
                ('x_school_end', models.CharField(max_length=40)),
                ('about_x_school', models.TextField()),
            ],
        ),
    ]
