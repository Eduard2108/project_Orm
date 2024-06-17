# Generated by Django 5.0.6 on 2024-06-15 00:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='detallenota',
            name='nota1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='detallenota',
            name='nota2',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='detallenota',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='detallenota',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nota',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='nota',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='periodo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='periodo',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='periodo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='periodo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profesor',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
