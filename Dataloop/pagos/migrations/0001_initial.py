# Generated by Django 3.2 on 2021-04-24 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gasto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('concepto', models.CharField(max_length=50)),
                ('fecha_aplicacion', models.DateField()),
                ('monto', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='recibo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('casa', models.IntegerField()),
                ('mes', models.SmallIntegerField()),
                ('monto', models.PositiveSmallIntegerField()),
                ('fecha_pago', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
