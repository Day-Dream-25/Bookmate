# Generated by Django 3.2.13 on 2022-05-02 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220423_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_city', to='user.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_state', to='user.state'),
        ),
    ]
