# Generated by Django 3.2.7 on 2021-09-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectMa_App', '0007_alter_mce_student_records_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mce_student_records',
            name='Member2_Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mce_student_records',
            name='Member3_Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mce_student_records',
            name='Member4_Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]