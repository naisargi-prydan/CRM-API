# Generated by Django 3.2.7 on 2021-09-18 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210918_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='stblAddressType',
            fields=[
                ('AddressTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('AddressType', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='tblentity',
            name='EntityTypeIDF',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.stblentitytype'),
        ),
        migrations.CreateModel(
            name='tblAddress',
            fields=[
                ('AddressID', models.AutoField(primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=1024)),
                ('City', models.CharField(max_length=30)),
                ('District', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('PinCode', models.IntegerField()),
                ('Country', models.CharField(max_length=30)),
                ('AddressTypeIDF', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.stbladdresstype')),
            ],
        ),
    ]
