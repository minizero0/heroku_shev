# Generated by Django 2.2.3 on 2019-11-26 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('easyvolunteer', '0012_cuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_job', to='easyvolunteer.Job', verbose_name='직업'),
        ),
    ]
