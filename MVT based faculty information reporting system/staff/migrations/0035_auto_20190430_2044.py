# Generated by Django 2.1.5 on 2019-04-30 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0034_auto_20190430_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grants_Applied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('projectname', models.CharField(max_length=600)),
                ('agency', models.CharField(max_length=600)),
                ('grantamount', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=900)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='grantsapplied4',
        ),
    ]
