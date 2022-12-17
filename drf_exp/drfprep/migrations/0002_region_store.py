# Generated by Django 3.2.5 on 2022-06-06 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drfprep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfprep.product')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=30)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drfprep.store')),
            ],
        ),
    ]
