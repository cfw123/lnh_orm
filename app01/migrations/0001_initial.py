# Generated by Django 2.0.4 on 2020-09-20 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pub_date', models.DateTimeField()),
                ('publish', models.CharField(max_length=32)),
            ],
        ),
    ]
