# Generated by Django 2.2.1 on 2019-06-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=20)),
                ('pname', models.CharField(max_length=100)),
                ('pemail', models.EmailField(max_length=254)),
                ('paddress', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'pharmacy',
            },
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=20)),
                ('tname', models.CharField(max_length=20)),
                ('tdate', models.DateField()),
                ('tquantity', models.IntegerField(default=0)),
                ('tprice', models.IntegerField(default=0)),
                ('ttprice', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tb',
            },
        ),
    ]
