# Generated by Django 4.2.6 on 2023-10-05 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doctorID',
        ),
        migrations.AddField(
            model_name='doctor',
            name='shiftType',
            field=models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(default='NA', max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='User.user'),
        ),
    ]
