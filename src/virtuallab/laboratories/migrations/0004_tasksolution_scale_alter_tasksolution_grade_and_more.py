# Generated by Django 5.0.3 on 2024-04-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratories', '0003_task_end_value_task_start_value_alter_laboratory_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksolution',
            name='scale',
            field=models.PositiveSmallIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='tasksolution',
            name='grade',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tasksolution',
            name='solution',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tasksolution',
            name='time_end',
            field=models.DateTimeField(null=True),
        ),
    ]
