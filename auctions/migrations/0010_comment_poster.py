# Generated by Django 3.1 on 2020-09-07 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200907_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='auctions.user'),
            preserve_default=False,
        ),
    ]
