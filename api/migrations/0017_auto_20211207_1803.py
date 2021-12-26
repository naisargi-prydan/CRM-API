# Generated by Django 3.2.7 on 2021-12-07 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0016_auto_20211207_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblperson',
            name='CompanyIDF',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tblcompany'),
        ),
        # migrations.AddField(
        #     model_name='tblperson',
        #     name='CreatedAT',
        #     field=models.DateTimeField(auto_now_add=True, default=1),
        #     preserve_default=False,
        # ),
        migrations.AddField(
            model_name='tblperson',
            name='CreatedBY',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
