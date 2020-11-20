# Generated by Django 2.1.15 on 2020-11-20 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('secret', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('secret', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('place', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('tel_num', models.IntegerField()),
                ('acount_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('arrive_time', models.DateTimeField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('work_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlaneType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('voyage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('arrivePort_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivePort_id', to='app.Airport')),
                ('startPort_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='startPort_id', to='app.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('status', models.CharField(max_length=64)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Flight')),
            ],
        ),
        migrations.CreateModel(
            name='Vip',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='VipLevel',
            fields=[
                ('level_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='vip',
            name='level_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.VipLevel'),
        ),
        migrations.AddField(
            model_name='plane',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PlaneType'),
        ),
        migrations.AddField(
            model_name='flight',
            name='plane_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Plane'),
        ),
        migrations.AddField(
            model_name='flight',
            name='route_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Route'),
        ),
        migrations.AddField(
            model_name='bill',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer'),
        ),
        migrations.AddField(
            model_name='bill',
            name='ticket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ticket'),
        ),
    ]