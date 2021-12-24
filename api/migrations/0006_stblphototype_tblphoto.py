# Generated by Django 3.2.7 on 2021-09-20 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210920_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='stblPhotoType',
            fields=[
                ('PhotoTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('PhotoType', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tblPhoto',
            fields=[
                ('PhotoID', models.AutoField(primary_key=True, serialize=False)),
                ('Photo', models.FileField(upload_to='')),
                ('EntityTypeIDF', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.stblentitytype')),
                ('PhotoTypeIDF', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.stblphototype')),
            ],
        ),
    ]
